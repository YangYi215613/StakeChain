import time
import copy

class Block:
    def __init__(self, transactions, lastHash, forger, blockCount):
        """
        transactions: 区块中交易
        lastHash: 前区块哈希
        forger: 区块铸造者
        blockCount: 第几个快
        """
        self.transactions = transactions
        self.lastHash = lastHash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''  # 区块签名

    @staticmethod
    def genesis():
        """生成创世区块"""
        genesisBlock = Block([], 'genesisHash', 'genesis', 0)
        genesisBlock.timestamp = 0
        return genesisBlock

    def toJson(self):
        data = {}
        data['lastHash'] = self.lastHash
        data['forger'] = self.forger
        data['blockCount'] = self.blockCount
        data['timestamp'] = self.timestamp
        data['signature'] = self.signature
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.toJson())
        
        data['transactions'] = jsonTransactions
        return data
    
    def payload(self):
        """区块中本身附带的数据"""
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def sign(self, signature):
        """区块签名"""
        self.signature = signature