from Transation import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from pprint import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel


if __name__ == '__main__':
    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()

    # EXCHANGE交易可以执行，但是TRANSFER逻辑上可以，但是因为EXCHANGE交易没有执行，所以TRANSFER交易也不能执行
    # 解决方式: 1 先执行 EXCHANGE交易，2 清空交易池中的特定交易 3 后执行 TRANSFER交易  4 清空交易池中的特定交易

    # 1 先执行 EXCHANGE交易
    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10, 'EXCHANGE')

    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)

    # 区块链中最后一个块的哈希
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # 新区块的编号
    blockCount = blockchain.blocks[-1].blockCount + 1
    # 生成blockOne区块，区块中包含EXCHANGE交易
    # blockOne = Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
    blockOne = forger.createBlock(coveredTransaction, lastHash, blockCount)  # 使用铸造者的钱包创建区块(同时进行签名)
    blockchain.addBlock(blockOne)

    # 2 清空交易池中的特定交易
    pool.removeFromPool(blockOne.transactions)

    # 3 后执行 TRANSFER交易
    transferTransaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')  # alice 向 bob 发送5个token

    if not pool.transactionExists(transferTransaction):
        pool.addTransaction(transferTransaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)

    # 区块链中最后一个块的哈希
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # 新区块的编号
    blockCount = blockchain.blocks[-1].blockCount + 1
    # 生成blockOne区块，区块中包含EXCHANGE交易
    # blockTwo = Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
    blockTwo = forger.createBlock(coveredTransaction, lastHash, blockCount)  # 使用铸造者的钱包创建区块(同时进行签名)
    blockchain.addBlock(blockTwo)    

    # 4 清空交易池中的特定交易
    pool.removeFromPool(blockTwo.transactions)

    pprint(blockchain.toJson())