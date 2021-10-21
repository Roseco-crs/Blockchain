#################################
##   Generating Block Hashes   ##
#################################

from datetime import datetime
from hashlib import sha256

class Block:

  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()
    
    
  def print_block(self):
    # prints block contents
    
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
    
  def generate_hash(self):
    # hash the blocks contents
    
    # First, I convert each item into string and put them in a list.
    block_contents = [str(self.timestamp), str(self.transactions), str(self.previous_hash)]
    # Secondly, I join each element of the list by seperating them with '  '
    block_contents = ' '.join(block_contents)
    
    # simple
    # block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)

    # hash the block_contents
    block_hash = sha256(block_contents.encode())

    return block_hash.hexdigest()

