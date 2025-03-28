# Based on: https://drlee.io/building-your-own-blockchain-in-python-a-step-by-step-guide-ec10ea6c976d

import hashlib

class Block:
    def __init__(self, index, timestamp, data, prior_hash=''):
        self.index = index  # The position of the block in the chain
        self.timestamp = timestamp  # When the block was created
        self.data = data  # The data
        self.prior_hash = prior_hash  # Hash of the previous block
        self.hash = self.create_hash()  # The hash of this block

    def create_hash(self):
        # Convert all the properties into a single string and encode it
        block_string = f"{self.index}{self.prior_hash}{self.timestamp}{self.data}".encode()

        return hashlib.sha256(block_string).hexdigest()

class Block_Chain:
    def __init__(self):
        # Initialize the chain with the genesis block
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block
        return Block(0, '2025-03-09', 'This is the first block', '0')