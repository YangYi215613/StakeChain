from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])

    node = Node(ip, port)
    node.startP2P()  # 启动P2P服务
    node.startAPI(apiPort)  # 启动RESTful服务

    # 测试 三个端口，分别执行下述命令
    # python main.py localhost 10001 5000
    # python main.py localhost 10002 5001
    # python interaction.py
    # http://localhost:5000/transactionPool  查看交易池状态
    # http://localhost:5001/transactionPool  查看交易池状态

    # http://localhost:5000/info
    # http://localhost:5000/blockchain
