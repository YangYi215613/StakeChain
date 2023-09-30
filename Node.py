from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils
import copy


class Node:
    def __init__(self, ip, port, key=None):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        # 节点可初始设置KEY值, 不适用自动生成
        if key is not None:
            self.wallet.fromKey(key)

    def startP2P(self):
        """启动socket"""
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)  # 方便P2P通讯

    def startAPI(self, apiPort):
        """启动RESTful API"""
        self.api = NodeAPI()
        self.api.injectNode(self)  # 将node注入nodeAPI中
        self.api.start(apiPort)

    def handelTransaction(self, transaction):
        """节点处理交易"""
        data = transaction.payload()
        signature = transaction.signature
        signerPublicKey = transaction.senderPublicKey
        # 验证交易是否有效
        signatureValid = Wallet.signatureValid(data, signature, signerPublicKey)
        transactionExists = self.transactionPool.transactionExists(transaction)
        # 判断交易是否已经在区块链中
        transactionInBlock = self.blockchain.transactionExists(transaction)
        if not transactionExists and not transactionInBlock and signatureValid:
            # 将交易添加到该节点的交易池中
            self.transactionPool.addTransaction(transaction)
            # 广播交易
            message = Message(self.p2p.socketConnector, 'TRANSACTION', transaction)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
            # 是否达到生成区块条件
            forgingRequired = self.transactionPool.forgerRequired()
            if forgingRequired:
                self.forge()

    def handleBlock(self, block):
        """节点处理区块"""
        forger = block.forger
        blockHash = block.payload()
        signature = block.signature

        blockCountValid = self.blockchain.blockCountValid(block)  # 验证区块数是否有效
        lastBlockHashValid = self.blockchain.lastBlockHashValid(block)   # 验证前区块哈希是否有效
        forgerValid = self.blockchain.forgerValid(block)  # 验证铸造者是否有效
        transactionValid = self.blockchain.transactionValid(block.transactions)  # 验证区块中交易是否有效
        signatureValid = Wallet.signatureValid(blockHash, signature, forger)  # 验证区块签名是否有效

        # 如果区块数目无效，向其余节点发送请求数据信息
        if not blockCountValid:
            self.requesetChain()

        if lastBlockHashValid and forgerValid and transactionValid and signatureValid and blockCountValid:
            # 该节点打包交易
            self.blockchain.addBlock(block)
            self.transactionPool.removeFromPool(block.transactions)
            # 广播交易
            message = Message(self.p2p.socketConnector, 'BLOCK', block)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)

    def requesetChain(self):
        """广播请求区块链数据消息"""
        message = Message(self.p2p.socketConnector, 'BLOCKCHAINREQUEST', None)
        encodedMessage = BlockchainUtils.encode(message)
        self.p2p.broadcast(encodedMessage)

    def handleBlockchainRequest(self, requestingNode):
        """给指定节点requestingNode发送自己本地区块数据"""
        message = Message(self.p2p.socketConnector, 'BLOCKCHAIN', self.blockchain)
        encodedMessage = BlockchainUtils.encode(message)
        self.p2p.send(requestingNode, encodedMessage)

    def handleBlockchain(self, blockchain):
        """进行增量数据同步"""
        localBlockchainCopy = copy.deepcopy(self.blockchain)
        localBlockCount = len(localBlockchainCopy.blocks)
        receivedChainBlockCount = len(blockchain.blocks)
        if localBlockCount < receivedChainBlockCount:
            for blockNumber, block in enumerate(blockchain.blocks):
                if blockNumber >= localBlockCount:
                    localBlockchainCopy.addBlock(block)
                    self.transactionPool.removeFromPool(block.transactions)
            self.blockchain = localBlockchainCopy

    def forge(self):
        """判断节点该节点是不是领导者"""
        forger = self.blockchain.nextForger()
        if forger == self.wallet.publicKeyString():
            # 生成区块
            print('我是下一个领导者')
            # 创建区块
            block = self.blockchain.createBlock(self.transactionPool.transactions, self.wallet)
            # 删除交易池中的交易
            self.transactionPool.removeFromPool(block.transactions)
            # 创建BLOCK交易
            message = Message(self.p2p.socketConnector, 'BLOCK', block)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
        else:
            print('我不是下一个领导者')
