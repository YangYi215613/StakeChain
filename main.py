from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2P()  

    # 测试: 三个终端，分别执行
    # python main.py localhost 10001 
    # python main.py localhost 10002
    # python main.py localhost 10003