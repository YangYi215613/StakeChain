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
        self.peerDiscoveryHandler.handshake(connected_node)
    
    def outbound_node_connected(self, connected_node):
       self.peerDiscoveryHandler.handshake(connected_node)

    def node_message(self, connected_node, message):
        print(message)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)