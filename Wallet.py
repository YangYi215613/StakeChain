from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transation import Transaction
from Block import Block

class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def fromKey(self, file):
        """从文件中导入密钥"""
        key = ''
        with open(file, 'r') as keyfile:
            key = RSA.importKey(keyfile.read())
        self.keyPair = key

    def sign(self, data):
        """签名数据"""
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        """验证签名数据"""
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.import_key(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid

    def publicKeyString(self):
        """生成公钥"""
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString
 
    def createTransaction(self, receiver, amount, type):
        """使用钱包创建交易"""
        transaction = Transaction(self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
    
    def createBlock(self, transactions, lastHash, blockCount):
        """使用钱包创建区块"""
        block = Block(transactions, lastHash, self.publicKeyString(), blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block