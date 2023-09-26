class AccountModel:
    def __init__(self):
        self.accounts = []
        self.balances = {}

    def addAccount(self, publicKeyString):
        """通过key添加value值"""
        if not publicKeyString in self.accounts:
            self.accounts.append(publicKeyString)
            self.balances[publicKeyString] = 0
    
    def getBalance(self, publicKeyString):
        """得到key的value值"""
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        return self.balances[publicKeyString]

    def updateBalance(self, publicKeyString, amount):
        """更新key的value值"""
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        
        self.balances[publicKeyString] += amount