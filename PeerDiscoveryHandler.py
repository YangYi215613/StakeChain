import threading
import time
from Message import Message
from BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler:
    def __init__(self, node):
        self.socketCommunication = node

    def status(self):
        while True:
            print('status')
            time.sleep(10) 
    
    def dicovery(self):
        while True:
            print('discovery')
            time.sleep(10)

    def start(self):
        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.dicovery, args=())
        discoveryThread.start()

    def handshake(self, connect_node):
        handshakeMessage = self.handshakeMessage()
        self.socketCommunication.send(connect_node, handshakeMessage)

    def handshakeMessage(self):
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = 'DISCOVERY'
        message = Message(ownConnector, messageType, data)
        encodeMessage = BlockchainUtils.encode(message)
        return encodeMessage