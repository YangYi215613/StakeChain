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

    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10, 'EXCHANGE')

    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    # alice 向 bob 发送5个token
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    # 此处有bug，EXCHANGE交易可以执行，但是TRANSFER逻辑上可以，但是因为EXCHANGE交易没有执行，所以TRANSFER交易也不能执行
    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)

    print(coveredTransaction)