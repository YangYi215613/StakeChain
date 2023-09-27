from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler


class SocketCommunication(Node):
    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []  
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
    
    def startSocketCommunication(self):
        self.start()  # 启动socket线程
        self.peerDiscoveryHandler.start()  # 启动节点发现

    def inbound_node_connected(self, connected_node):
        print('inbound connection')
        self.send_to_node(connected_node, '你好，我是你链接的节点')
    
    def outbound_node_connected(self, connected_node):
        print('outbound connection')
        self.send_to_node(connected_node, '你好，我是要链接你的节点')

    def node_message(self, connected_node, message):
        print(message)