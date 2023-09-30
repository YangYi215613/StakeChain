class Message:
    """网络中传播消息类型"""
    def __init__(self, senderConnector, messageType, data):
        self.senderConnector = senderConnector  # 发起方
        self.messageType = messageType  # 消息类型
        self.data = data  # 数据