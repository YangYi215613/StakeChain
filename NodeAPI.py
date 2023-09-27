from flask_classful import FlaskView, route
from flask import Flask, jsonify, request
from BlockchainUtils import BlockchainUtils

node = None

class NodeAPI(FlaskView):
    def __init__(self):
        self.app = Flask(__name__)

    def start(self, apiPort):
        NodeAPI.register(self.app, route_base='/')
        self.app.run(host='localhost', port=apiPort)

    def injectNode(self, injectedNode):
        """
        node可以访问nodeAPI，反之不行
        但nodeAPI需要返回node的信息，所以构建此函数
        """
        global node
        node = injectedNode

    @route('/info', methods=['GET'])
    def info(self):
        """测试接口"""
        return 'This is a communication interface to a node blockchain', 200

    @route('/blockchain', methods=['GET'])
    def blockchain(self):
        """查看节点中区块链数据"""
        return node.blockchain.toJson(), 200

    @route('/transactionPool', methods=['GET'])
    def transactionPool(self):
        """查看节点中区块池数据"""
        transactions = {}
        for number, transaction in enumerate(node.transactionPool.transactions):
            transactions[number] = transaction.toJson()
        return jsonify(transactions), 200

    @route('/transaction', methods=['POST'])
    def transaction(self):
        """发起交易"""
        values = request.get_json()
        if not 'transaction' in values:
            return 'Missing transaction value', 400
        # 解码成交易信息
        transaction = BlockchainUtils.decode(values['transaction'])
        # 处理交易
        node.handelTransaction(transaction)
        response = {'message': 'Received transaction'}

        return jsonify(response), 201