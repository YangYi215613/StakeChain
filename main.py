from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2P()  # 启动P2P服务
    node.startAPI()  # 启动RESTFUL服务

    # 测试
    # http://localhost:5000/info