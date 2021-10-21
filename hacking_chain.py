###########################
##   Hacking the Chain   ##
###########################



from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# Instantiate a new Blockchain object
my_blockchain = Blockchain()

# Add a new block to my_blockchain
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

#my_blockchain.validate_chain()

# transactions of block 1 in my_blockchain is assigned "fake_transactions". 
# Here, I hack the chain and it return mismatch message after validating.
my_blockchain.chain[1].transactions = 'fake_transactions'
my_blockchain.validate_chain()

