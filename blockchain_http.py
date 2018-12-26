import time
import json
import hashlib
class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(proof=100, previous_hash=0)

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
