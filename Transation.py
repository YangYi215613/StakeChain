import uuid
import time
import copy


class Transaction:
    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        """
        senderPublicKey: 发送者公钥
        receiverPublicKey: 接收者公钥
        amount: 交易数
        type: 交易类型
        id: uuid
        timestamp: 时间戳
        signature: 交易签名
        """
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex 
        self.timestamp = time.time()
        self.signature = '' 

    def toJson(self):
        """交易字典形式"""
        return self.__dict__
    
    def sign(self, signature):
        """交易签名"""
        self.signature = signature

    def payload(self):
        """返回数据原始payload"""
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def equals(self, transaction):
        """判断交易是否相等，通过uuid"""
        if self.id == transaction.id:
            return True
        else:
            return False