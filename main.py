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

    # alice 向 bob 发送5个token
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)

    print(coveredTransaction)