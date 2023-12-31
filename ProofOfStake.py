from Lot import Lot
from BlockchainUtils import BlockchainUtils

class ProofOfStake:
    def __init__(self):
        """
        key: 公钥
        value: 抵押数
        """
        # stakesr如果没有数据，导致没有办法选择铸造者，执行会出错
        self.stakes = {}
        self.setGenesisNodeStake()

    def setGenesisNodeStake(self):
        """设置初始权益抵押，否则无法生成铸造者，打包第一个区块，触发后续状态的更改"""
        genesisPublicKey = open('./keys/genesisPublicKey.pem', 'r').read()
        self.stakes[genesisPublicKey] = 1

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

    def _validatorLots(self, seed):
        lots = []
        for validator in self.stakes.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        
        return lots

    def _winnerLot(self, lots, seed):
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
        """返回PoS领导者的公钥"""
        lots = self._validatorLots(lastBlockHash)
        winnerLot = self._winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey