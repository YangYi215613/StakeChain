from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain


class Node:
    def __init__(self):
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()