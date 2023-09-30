import threading
import time
from Message import Message
from BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler:
    def __init__(self, node):
        self.socketCommunication = node

    def _status(self):
        """每 10 秒打印一次所有连接节点的列表"""
        while True:
            print('Current Connection:')
            for peer in self.socketCommunication.peers:
                print(str(peer.ip) + ':' + str(peer.port))
            time.sleep(10) 
    
    def _dicovery(self):
        """每 10 秒向所有连接的节点广播握手消息"""
        while True:
            handshakeMessage = self.handshakeMessage()
            self.socketCommunication.broadcast(handshakeMessage)
            time.sleep(10)

    def start(self):
        """使用两个单独的线程进行状态监控和节点发现"""
        statusThread = threading.Thread(target=self._status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self._dicovery, args=())
        discoveryThread.start()

    def handshake(self, connect_node):
        """向特定节点发送握手消息"""
        handshakeMessage = self.handshakeMessage()
        self.socketCommunication.send(connect_node, handshakeMessage)

    def handshakeMessage(self):
        """创建握手消息"""
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = 'DISCOVERY'
        message = Message(ownConnector, messageType, data)
        encodeMessage = BlockchainUtils.encode(message)
        return encodeMessage

def handleMessage(self, message):
    """处理来自其他节点的握手消息"""
    peersSocketConnector = message.senderConnector
    peersPeerList = message.data
    newPeer = True
    
    # 检查是否为新节点
    for peer in self.socketCommunication.peers:
        if peer.equals(peersSocketConnector):
            newPeer = False
    
    if newPeer:
        # 将发送方的连接器对象添加到节点的连接器列表中
        self.socketCommunication.peers.append(peersSocketConnector)
    
    for peersPeer in peersPeerList:
        peerKnown = False
        
        # 检查是否已知节点
        for peer in self.socketCommunication.peers:
            if peer.equals(peersPeer):
                peerKnown = True
        
        # 如果节点未知且不是自身节点，则与其建立连接
        if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
            self.socketCommunication.connect_with_node(peersPeer.ip, peersPeer.port)