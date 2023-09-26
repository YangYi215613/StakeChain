from Crypto.Hash import SHA256
import jsonpickle

class BlockchainUtils():
    @staticmethod
    def hash(data):
        """
        返回数据的sha256哈希值
        """
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

    @staticmethod
    def encode(objectToEncode):
        return jsonpickle.encode(objectToEncode, unpicklable=True)

    @staticmethod
    def decode(encodedObject):
        return jsonpickle.decode(encodedObject)