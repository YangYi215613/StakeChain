from BlockchainUtils import BlockchainUtils

class Lot:
    def __init__(self, publicKey, iteration, lastBlockHash):
        self.publicKey = str(publicKey)
        self.iteration = iteration
        self.lastBlockHash = lastBlockHash
        
    def lotHash(self):
        # 将公钥和上一个区块的哈希值拼接
        hashData = self.publicKey + self.lastBlockHash
        # 迭代计算哈希值
        for _ in range(self.iteration):
            hashData = BlockchainUtils.hash(hashData).hexdigest()
        return hashData