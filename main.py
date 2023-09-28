from Node import Node
import sys


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])

    keyFile = None
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    node = Node(ip, port, key=keyFile)
    node.startP2P()  # 启动P2P服务
    node.startAPI(apiPort)  # 启动RESTful服务


    # http://localhost:5000/transactionPool  查看交易池状态
    # http://localhost:5001/transactionPool  查看交易池状态

    # http://localhost:5000/info
    # http://localhost:5000/blockchain
 