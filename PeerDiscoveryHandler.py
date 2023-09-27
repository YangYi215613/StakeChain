import threading
import time

class PeerDiscoveryHandler:
    def __init__(self, node):
        self.SocketCommunication = node

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
        self.SocketCommunication.send(connect_node, 'HandShake ...')