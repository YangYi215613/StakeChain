from Crypto.Hash import SHA256
import jsonpickle

class BlockchainUtils():
    @staticmethod
    def hash(data):
        """
        返回数据的sha256哈希值
        """
        dataString = jsonpickle.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

    @staticmethod
    def encode(objectToEncode):
        """编码数据"""
        return jsonpickle.encode(objectToEncode, unpicklable=True)

    @staticmethod
    def decode(encodedObject):
        """解码数据"""
        return jsonpickle.decode(encodedObject)