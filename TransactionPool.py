class TransactionPool():
    def __init__(self):
        self.transactions = []
    
    def addTransaction(self, transaction):
        """交易池中添加交易"""
        self.transactions.append(transaction)

    def transactionExists(self, transaction):
        """判断交易是否存在交易池中"""
        for poolTransaction in self.transactions:
            if poolTransaction.equals(transaction):
                return True
        return False