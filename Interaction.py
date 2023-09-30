"""
交互文件: 通过RESTful向区块链网络中发送交易
"""
from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


def postTransaction(sender, receiver, amount, type):
    """
    sender: 发送者钱包
    receiver: 接受者钱包
    amount: 转账数目
    type: 交易类型
    """
    transaction = sender.createTransaction(receiver.publicKeyString(), amount, type)
    url = url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)  # '{'message': 'Received transaction'}'

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    alice.fromKey(file='keys/stakerPrivateKey.pem')
    exchange = Wallet()

    # 铸造者: genesis
    postTransaction(exchange, alice, 100, 'EXCHANGE')
    postTransaction(exchange, bob, 100, 'EXCHANGE')
    postTransaction(alice, alice, 25, 'STAKE')  # alice抵押25token

    # pos之后，铸造者: 可能是 alice
    postTransaction(alice, bob, 1, 'TRANFER')
