import uuid
import time

class Transaction:
    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        """
        senderPublicKey: 发送者公钥
        receiverPublicKey: 接收者公钥
        amount: 交易数
        type: 交易类型
        """
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex  # 交易ID
        self.timestamp = time.time()
        self.signature = ''  # 签名

    def toJson(self):
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature