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
        """区块添加到本地区块链副本"""
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
        if transaction.type == 'STAKE':
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            if sender == receiver:
                amount = transaction.amount
                # 更新抵押数
                self.pos.update(sender, amount)
                # 修改账户余额(抵押之后，余额变低)
                self.accountModel.updateBalance(sender, -amount)
        else:
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

    def createBlock(self, transactionFromPool, forgerWallet):
        """创建区块"""
        coveredTransactions = self.getCoveredTransactionSet(transactionFromPool)
        self.executeTransactions(coveredTransactions)
        newBlock = forgerWallet.createBlock(coveredTransactions, BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(), len(self.blocks))
        self.blocks.append(newBlock)
        return newBlock

    def transactionExists(self, transaction):
        """判断交易是否已经在区块链中(如果在区块链中，就不添加该交易)"""
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if transaction.equals(blockTransaction):
                    return True
        return False

    def forgerValid(self, block):
        """验证领导者是否有效"""
        forgerPublicKey = self.pos.forger(block.lastHash)
        proposeBlockForger = block.forger
        if forgerPublicKey == proposeBlockForger:
            return True
        else:
            return False

    def transactionValid(self, transactions):
        """验证交易是否有效"""
        coveredTransactions = self.getCoveredTransactionSet(transactions)
        if len(coveredTransactions) == len(transactions):
            return True
        else:
            return False
        