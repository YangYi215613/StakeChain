from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel


class Blockchain:

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()

    def addBlock(self, block):
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data

    def blockCountValid(self, block):
        """验证区块计数"""
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False

    def lastBlockHashValid(self, block):
        """验证上一个区块哈希"""
        lastBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()

        if lastBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False

    def transactionCovered(self, transaction):
        """判断交易数目是否超出"""
        sendBalance = self.accountModel.getBalance(transaction.senderPublicKey)

        if sendBalance >= transaction.amount:
            return True
        else:
            return False

    def getCoveredTransactionSet(self, transactions):
        """得到transactions中符合的transaciton"""
        coveredTransactions = []

        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print('Transaction is not covered by sender')
        
        return coveredTransactions