import threading
import time
from Message import Message
from BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler:
    def __init__(self, node):
        self.socketCommunication = node

    def status(self):
        while True:
            print('Current Connection:')
            for peer in self.socketCommunication.peers:
                print(str(peer.ip) + ':' + str(peer.port))
            time.sleep(10) 
    
    def dicovery(self):
        while True:
            handshakeMessage = self.handshakeMessage()
            self.socketCommunication.broadcast(handshakeMessage)
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

    def handleMessage(self, message):
        peersSocketConnector = message.senderConnector
        peersPeerList = message.data
        newPeer = True
        for peer in self.socketCommunication.peers:
            if peer.equals(peersSocketConnector):
                newPeer = False
        
        if newPeer == True:
            self.socketCommunication.peers.append(peersSocketConnector)
        
        for peersPeer in peersPeerList:
            peerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peersPeer):
                    peerKnown = True
            
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.connect_with_node(peersPeer.ip, peersPeer.port)