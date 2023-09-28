from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from BlockchainUtils import BlockchainUtils
import json


class SocketCommunication(Node):
    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []  
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip, port)
    
    def connectFirstNode(self):
        if not self.socketConnector.port == 10001:
            self.connect_with_node('localhost', 10001)

    def startSocketCommunication(self, node):
        self.node = node
        self.start()  # 启动socket线程
        self.peerDiscoveryHandler.start()  # 启动节点发现
        self.connectFirstNode()

    def inbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)
    
    def outbound_node_connected(self, connected_node):
       self.peerDiscoveryHandler.handshake(connected_node)

    def node_message(self, connected_node, message):
        # 处理p2p网络中的消息
        message = BlockchainUtils.decode(json.dumps(message))
        if message.messageType == 'DISCOVERY':
            self.peerDiscoveryHandler.handleMessage(message)
        elif message.messageType == 'TRANSACTION':
            transaction = message.data
            self.node.handelTransaction(transaction)
        elif message.messageType == 'BLOCK':
            block = message.data
            self.node.handleBlock(block)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)