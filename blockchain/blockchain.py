import time
import hashlib


class Block(object):

    def __init__(self, index, proof, previous_hash, transactions, timestamp=None):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()

    @property
    def get_block_hash(self):
        block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)
    

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_node_transactions = []
        self.nodes = set()
        self.create_genesis_block()    # for initialization of the blockchain

    @property
    def get_serialized_chain(self):
        return [vars(block) for block in self.chain]
    
    def create_genesis_block(self):
        self.create_new_block(proof=0, previous_hash=0)

    def create_new_block(self,proof,previous_hash):
        block = Block(
            index = len(self.chain),
            proof = proof,
            previous_hash = previous_hash,
            transactions = self.current_node_transactions,
            )
        self.current_node_transactions = []  # Reset the transaction list

        self.chain.append(block)
        return block

    @staticmethod
    def is_valid_block(block, previous_block):
        if previous_block.index + 1 != block.index:
            return False
        elif previous_block.get_block_hash != block.previous_hash:
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False

        return True
    
    def create_new_transaction(self, sender, recipient, amount):
        self.current_node_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            })

        return True

    @staticmethod
    def is_valid_transaction():
        # Not implemented
        pass
    

    @staticmethod
    def create_proof_of_work(previous_proof):
        """
        Generate "Proof of work"
        A very simple Proof of work algorithm
        Find a number such that, sum of the number and previous POW number is
        divisible by 7
        """
        proof = previous_proof + 1
        while (proof + previous_proof) % 7 != 0:
            proof += 1

        return proof

    @staticmethod
    def is_valid_proof(proof, previous_proof):
        return (proof + previous_proof) % 7 == 0

    @property
    def get_last_block(self):
        return self.chain[-1]

    def is_valid_chain(self):
        """
        Check if given blockchain is valid
        """
        previous_block = self.chain[0]
        current_index = 1

        while current_index < len(self.chain):
            block = self.chain[current_index]
            if not self.is_valid_block(block, previous_block):
                return False

            previous_block = block
            current_index += 1

        return True

    def mine_block(self, miner_address):
        # Sender 0 means that this node has mined a new block
        # For mining the Block(or finding the proof), we must award with some
        # amount(in our case this is 1)
        self.create_new_transaction(
            sender="0",
            recipient=miner_address,
            amount=1,
            )
        last_block = self.get_last_block

        last_proof = last_block.proof
        proof = self.create_proof_of_work(last_proof)

        last_hash = last_block.get_block_hash
        block = self.create_new_block(proof, last_hash)

        return vars(block)  # Return a native dict type object

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def get_block_object_from_block_data(block_data):
        return Block(
            block_data['index'],
            block_data['proof'],
            block_data['previous_hash'],
            block_data['transactions'],
            timestamp=block_data['timestamp'],
            )
    

# Creating the Http API

from argparse import ArgumentParser
from uuid import uuid4
from flask import Flask, jsonify


app = Flask(__name__)

blockchain = Blockchain()

node_address = uuid4().hex

@app.route('/create-transaction', methods=['POST'])
def create_transaction():
    transaction_data = request.get_json() #Accepting payload from the user in Json format
    index = blockchain.create_new_transaction(**transaction_data)

    response = {
        'message': 'Transaction has been submitted successfully',
        'block_index': index
        }
    return jsonify(response), 201


@app.route('/mine', methods=['GET'])
def mine():
    block = blockchain.mine_block(node_address)

    response = {
        'message': 'Successfully Mined the new block',
        'block_data' : block
        }
    return jsonify(response)

@app.route('/chain', methods=['GET'])
def get_full_chain():
    response = {
        'chain': blockchain.get_serialized_chain,
        }
    return jsonify(response)





parser = ArgumentParser()
parser.add_argument('-H', '--host', default='127.0.0.1')
parser.add_argument('-p', '--port', default=5000, type=int)
args = parser.parse_args()

app.run(host=args.host, port=args.port, debug=True)

