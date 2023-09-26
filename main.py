from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2P()  # python main.py localhost 5000