from Transation import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from pprint import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(receiver, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)


    blockchain = Blockchain()

    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)

    if not blockchain.lastBlockHashValid(block):
        print('区块中不是有效的前区块哈希')
    
    if not blockchain.blockCountValid(block):
        print('区块中区块计数不有效')

    if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
        blockchain.addBlock(block)

    pprint(blockchain.toJson())
