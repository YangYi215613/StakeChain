from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake


class Blockchain:

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()
        self.pos = ProofOfStake()

    def addBlock(self, block):
        self.executeTransactions(block.transactions)  # 执行区块中的交易
        
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
        if transaction.type == 'EXCHANGE': return True

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

    def executeTransaction(self, transaction):
        """执行单笔交易"""
        sender = transaction.senderPublicKey
        receiver = transaction.receiverPublicKey
        amount = transaction.amount
        self.accountModel.updateBalance(sender, -amount)
        self.accountModel.updateBalance(receiver, amount)

    def executeTransactions(self, transactions):
        """执行多笔交易"""
        for transaction in transactions:
            self.executeTransaction(transaction)

    def nextForger(self):
        """生成下一个铸造者"""
        lastBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        nextForger = self.pos.forger(lastBlockHash)
        return nextForger