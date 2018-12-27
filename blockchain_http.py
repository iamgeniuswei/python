import time
import json
import hashlib
from urllib.parse import urlparse
import requests


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.new_block(proof=100, previous_hash=0)

    def register_node(self, address):
        """
        Add a new node the list of nodes
        :param address: <str> The node's address Eg. 'http://192.168.0.5:5000'
        :return None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A block chain
        :return: <bool> True if valid, False if not
        """    
        try:
            last_block = chain[0]
            current_index = 1
            while current_index < len(chain):
                block = chain[current_index]
                print(f'{last_block}')
                print(f'{block}')
                print("\n-----------\n")
                #check the block's hash
                if block['previous_hash'] != self.hash(last_block):
                    return False
                
                #check the proof of work
                if not self.valid_proof(last_block['proof'], block['proof']):
                    return False
                
                last_block = block
                current_index += 1
            return True     
        except Exception as e:
            print(str(e))
            return False        


    def resolve_confilicts(self):
        """
        A simple consensus algorithm, which resolves conflicts by replacing our chain with
        the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """
        neighbours = self.nodes
        new_chain = None
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                #check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        
        if new_chain:
            self.chain = new_chain
            return True
        return False

    def new_block(self, proof, previous_hash = None):
        # Creates a new Block and adds to the chain
        """
        :param proof: <int> proof of work
        :param previous_hash: (Optional) <str> the hash of previous block
        :return: <dict> The new block
        """
        
        block = {
                'index': len(self.chain),
                'timestamp': time.time(),
                'transaction': self.current_transactions,
                'proof': proof,
                'previous_hash': previous_hash
            }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amout):
        # Adds a new transaction to the list of transactions
        """
        :param sender: <str> Address of Sender
        :param recipient: <str> Address of recipient
        :param amout: <int> Amout
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient':recipient,
            'amout':amout
        })
        return self.last_block['index']+1

    @staticmethod
    def hash(block):
        # Hashes a block
        """
        :param block: <dict> Block
        :return: <str> hash of block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm.
        Find a
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1        
        return proof


    @staticmethod
    def valid_proof(last_proof, proof):
        """
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
