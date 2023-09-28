from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils


class Node:
    def __init__(self, ip, port, key=None):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        if key is not None:
            self.wallet.fromKey(key)

    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)  # 方便P2P通讯

    def startAPI(self, apiPort):
        self.api = NodeAPI()
        self.api.injectNode(self)  # 将node注入nodeAPI中
        self.api.start(apiPort)

    def handelTransaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signerPublicKey = transaction.senderPublicKey
        # 验证交易是否有效
        signatureValid = Wallet.signatureValid(data, signature, signerPublicKey)
        transactionExists = self.transactionPool.transactionExists(transaction)
        if not transactionExists and signatureValid:
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
    
    def forge(self):
        forger = self.blockchain.nextForger()
        if forger == self.wallet.publicKeyString():
            # 生成区块
            print('我是下一个铸造者')
        else:
            print('我不是下一个铸造者')
