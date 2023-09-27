from flask_classful import FlaskView, route
from flask import Flask, jsonify

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
        return 'This is a communication interface to a node blockchain', 200

    @route('/blockchain', methods=['GET'])
    def blockchain(self):
        return node.blockchain.toJson(), 200

    @route('/transactionPool', methods=['GET'])
    def transactionPool(self):
        transactions = {}
        for number, transaction in enumerate(node.transactionPool.transactions):
            transactions[number] = transaction.toJson()
        return jsonify(transactions), 200