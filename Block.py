import time

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
        