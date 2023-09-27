from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])

    node = Node(ip, port)
    node.startP2P()  # 启动P2P服务
    node.startAPI(apiPort)  # 启动RESTful服务

    # 测试
    # python main.py localhost 10001 5001
    # http://localhost:5001/info