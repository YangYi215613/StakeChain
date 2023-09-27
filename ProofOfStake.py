from Lot import Lot
from BlockchainUtils import BlockchainUtils

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

    def validatorLots(self, seed):
        lots = []
        for validator in self.stakes.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        
        return lots

    def winnerLot(self, lots, seed):
        winnerLot = None
        leastOffSet = None
        referenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)

        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - referenceHashIntValue)
            if leastOffSet is None or offset < leastOffSet:
                leastOffSet = offset
                winnerLot = lot
        return winnerLot
    
    def forger(self, lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey