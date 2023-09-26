from Transation import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from pprint import pprint
from Blockchain import Blockchain

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

    block = wallet.createBlock(pool.transactions, 'lastHash', 1)

    blockchain = Blockchain()
    blockchain.addBlock(block)
    pprint(blockchain.toJson())