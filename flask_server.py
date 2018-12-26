from blockchain_http import *
from flask import Flask, jsonify, request
from uuid import uuid4
from textwrap import dedent
import json


# Instantiate our Node
app = Flask(__name__)


#Generate a global unique address for node
node_id = str(uuid4()).replace('-','')


#Instantiate the BlockChain
blockchain = BlockChain()


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender='0',
        recipient=node_id,
        amout=1
    )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transaction'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    try:
        values = request.get_json()
        required = ['sender', 'recipient', 'amout']
        if not all(k in values for k in required):
            return "Missing values", 400

        index = blockchain.new_transaction(
            values['sender'],
            values['recipient'],
            values['amout']
        )
        response = {
            'message': f'Transaction will be added to Block {index}'
        }
    except Exception as e:
        response = {
            'message': str(e)
        }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

