from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2P()  # python main.py localhost 5000

    if port == 10002:
        node.p2p.connect_with_node('localhost', 10001)

    # python main.py localhost 10001
    # python main.py localhost 10002