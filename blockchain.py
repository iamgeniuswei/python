
import time
import random
import hashlib


class BlockChain(object):
    def __init__(self, hash_num):
        self.chain_list = []
        self.result_list = []

        self.gen_block(hash_num)

    def get_last_block(self):
        if len(self.chain_list):
            return self.chain_list[-1]
        return None

    def get_trans(self):
        return "transaction"

    def gen_block(self, initial_hash = None):
        if initial_hash:
            block = Block()
            block.index = 0
            block.nonce = random.randrange(1, 99999)
            block.previous_hash = '0'
            block.difficulty = 0
            block.transaction = self.get_trans()

            guess = str(block.index) + str(block.nonce) + block.previous_hash
            block.hash = hashlib.sha256(guess.encode()).hexdigest()
            block.timestamp = time.time()
            self.chain_list.append(block)
            print(block.get_block_info())
        else:
            pitman = Pitman()
            last = self.get_last_block()
            last_info = last.get_block_info()
            hash = last_info['Hash']
            block, spend = pitman.mine(
                len(self.chain_list), 
                hash,
                self.get_trans()
            )
            self.chain_list.append(block)
            print(block.get_block_info())

class Block(object):    
    def __init__(self):
        self.index = None
        self.hash = None
        self.previous_hash = None
        self.nonce = None
        self.difficulty = None
        self.timestamp = None
        self.transaction = None

    def get_block_info(self):
        block_info = {
            'Index': self.index,
            'Hash': self.hash,
            'Previous_hash': self.previous_hash,
            'Nonce': self.nonce,
            'Difficulty': self.difficulty,
            'Timestamp': self.timestamp,
            'Transaction': self.transaction            
        }
        return block_info


class Pitman(object):
    def gen_hash(self, previous_hash, transaction):
        nonce = random.randrange(1, 99999)
        difficulty = 0
        guess = str(previous_hash) + str(nonce) + transaction
        res = hashlib.sha256(guess.encode()).hexdigest()

        #set difficulty, res[-1] == 0
        while res[-1] != '0' and res[-2] != '0':
            difficulty += 1
            nonce += difficulty
            guess = str(previous_hash) + str(nonce) + transaction
            res = hashlib.sha256(guess.encode()).hexdigest()

        return difficulty, res, nonce


    def mine(self, index, previous_hash, transaction):
        print("start mine...")
        begin_time = time.time()

        block = Block()
        block.index = index
        block.previous_hash = previous_hash
        block.transaction = transaction
        block.timestamp = time.time

        block.difficulty, block.hash, block.nonce = self.gen_hash(previous_hash, transaction)

        end_time = time.time()
        spend_time = end_time - begin_time
        print("end mine..., spend time: ", spend_time)
        
        return block, spend_time


if __name__ == '__main__':
    chain = BlockChain(1)
    for i in range(20):
        chain.gen_block()