# 定义SocketConnector类
class SocketConnector:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # 检查两个连接器是否相等
    def equals(self, connector):
        # 判断IP和端口是否相等
        if connector.ip == self.ip and connector.port == self.port:
            return True
        else:
            return False