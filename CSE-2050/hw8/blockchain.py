import hashmap
class Transaction():
    def __init__(self, from_user, to_user, amount):
        """ contains a single transaction of HuskyCoin: the sending user, the receiving user, and the amount being transferred """
        # removes amount from a user
        from_user.transfer(amount)
        # sends an amount to a user
        to_user.deposit(amount)

class Block():
    def __init__(self, transactions = None, previous_hash = None):
        """ contains a collection of transaction objects. Each block can contain N number of transactions
        Contains the hash of the previous block in the chain """
        # makes a 
        self.transactions = transactions if transactions else []
        self.previous_hash = previous_hash
    
    def add_transaction(self, transaction):
        """ adds a single transaction to the block and updates previous hash """
        self.transactions.append(transaction)

class Ledger():
    def __init__(self):
        """ contains an instance of your Hashmap ADT that will be used to keep track of user balances """
        self._hashmap = {}
    
    def has_funds(self, user, amount):
        if user not in self._hashmap:
            return False
        balance = self._hashmap[user]
        return balance >= amount

    def deposit(self, user, amount):
        """ adds an amount of HuskyCoin to the given user """
        if user in self._hashmap:
            self._hashmap[user] += amount
        else:
            self._hashmap[user] = amount

    def transfer(self, from_user, to_user, amount):
        """ subtracts an amount of HuskyCoin from the given user """
        if self.has_funds(from_user, amount):
            self._hashmap[from_user] -= amount
            self.deposit(to_user, amount)
            return True
        else:
            return False

class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = []     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    def add_block(self, transactions):
        """
        1. Store the hash of the previous block in the block being added
        2. Make sure users transferring HuskyCoin have the required balance. Do not allow
        the block to be added if any given transaction does not have required user funds.
        If any transaction is invalid, either throw an error or return False. But your other
        code
        """
        # get the hash of the previous block in the chain
        prev_block_hash = self.chain[-1].hash
        # mine a new block using the previous block hash and the transactions provided
        block = Block.mine_block(prev_block_hash, transactions)
        # check if the transactions are valid before adding the block
        if not self.ledger.validate_transactions(block.transactions):
            # if any transaction is invalid, return False to indicate that the block was not added
            return False
        # update the ledger with the transactions in the new block
        self.ledger.update_ledger(block.transactions)
        # add the new block to the chain
        self.chain.append(block)
        # return True to indicate that the block was successfully added
        return True
    
    def validate_chain(self):
        """
        1. Check to see if any of the blocks have been “tampered” with by comparing the
        hashes of each block in the chain are still correct.
        2. In your testng of this method, verify that if you try and modify any data value
        with a given transaction with a given block, that the validate_chain() method will
        detect the modification.
        3. Return a list of blocks that have been “tampered” with.
        """
        # list of tampered blocks
        tampered_blocks = []
        # iterate over the blockchain, starting from the second block
        for i in range(1, len(self.chain)):
            curr_block = self.chain[i]
            prev_block = self.chain[i-1]
            # check if the stored previous hash matches the actual hash of the previous block
            if curr_block.prev_hash != prev_block.hash:
                # if they don't match, the block has been tampered with, so add it to the list
                tampered_blocks.append(curr_block)
        # return the list of tampered blocks (could be empty)
        return tampered_blocks