from Transation import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from pprint import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel


if __name__ == '__main__':
    wallet = Wallet()
    accountModel = AccountModel()
    accountModel.updateBalance(wallet.publicKeyString(), 10)
    accountModel.updateBalance(wallet.publicKeyString(), -5)

    print(accountModel.balances)