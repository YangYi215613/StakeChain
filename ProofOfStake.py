class ProofOfStake:
    def __init__(self):
        """
        key: 公钥
        value: 抵押数
        """
        self.stakes = {}

    def update(self, publiKeyString, stake):
        if publiKeyString in self.stakes.keys():
            self.stakes[publiKeyString] += stake
        else:
            self.stakes[publiKeyString] = stake

    def get(self, publicKeyString):
        if publicKeyString in self.stakes.keys():
            return self.stakes[publicKeyString]
        else:
            return None