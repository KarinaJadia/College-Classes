import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    

    # starting here
    def add_left(self, node):
        """ adds a node on the left side """
        self.left = node

    def add_right(self, node):
        """ adds a node on the right side """
        self.right = node

    def evaluate(self):
        """ recursively evaluates the tree by going through and returning either the specific card or the operation, and then building it back up """
        # if the current node is an operator, recursively evaluate the left and right subtrees
        if self.value in BETNode.OPERATORS:
            # if it's not a number, recursively go until it reaches a number
            left_value = self.left.evaluate()
            right_value = self.right.evaluate()

            # perform the operation specified by the operator.
            if self.value == '+':
                return left_value + right_value
            elif self.value == '-':
                return left_value - right_value
            elif self.value == '*':
                return left_value * right_value
            elif self.value == '/':
                if right_value == 0 or right_value == float('inf'):
                    return float('inf')
                return left_value / right_value
        # division by zero results in an error but since that's not allowed, i turned it into infinity so it would work
        elif self.value == '0':
            return float('inf')
        elif self.value in BETNode.CARD_VAL_DICT:
            # if the current node is a card value, return its numeric value
            return BETNode.CARD_VAL_DICT[self.value]
        else:
            raise RuntimeError("something went wrong")
    
    def __repr__(self):
        """ recursively prints the tree """
        if self.value in BETNode.OPERATORS:
            left_str =  repr(self.left)
            right_str = repr(self.right)
            return "(" + left_str + self.value + right_str + ")"
        else:
            return str(self.value)


def create_trees(cards):
    ''' takes in a list of cards and returns a set of all possible combinations of binary trees that can be created using the given cards and operators '''
    # creates an empty set to hold all potential hands
    handset = set()
    # create a set to hold all possible binary trees
    treeset = set()
    # generates all possible combinations of operators
    poops = list(itertools.product(BETNode.OPERATORS, repeat = 3))

    # loops through each combination of operators (it's called poops because PoOps stands for Potential Operations)
    for op in poops:
        # generates all possible permutations of cards and operators
        potential_card = list(op)
        potential_card += cards
        all_hands = itertools.permutations(potential_card)
        # filters out only those permutations that are valid tree structures
        for hand in all_hands:
            if hand[0] in BETNode.CARD_VAL_DICT and hand[1] in BETNode.CARD_VAL_DICT and hand[6] in BETNode.OPERATORS:
                if hand[2] in BETNode.OPERATORS and hand[3] in BETNode.CARD_VAL_DICT:
                    handset.add(hand)
                elif hand[2] in BETNode.CARD_VAL_DICT and hand[3] in BETNode.OPERATORS:
                    handset.add(hand)
                elif hand[2] in BETNode.CARD_VAL_DICT and hand[3] in BETNode.CARD_VAL_DICT:
                    handset.add(hand)
    
    # creates binary trees for each valid permutation and add them to treeset
    for hand in handset:
        stack = []
        for card in hand:
            # if the node is a card, creates a new BETNode object and add it to the stack
            if card in BETNode.CARD_VAL_DICT:
                stack.append(BETNode(card))
            # if the node is an operator, creates a new BETNode object and add the two top nodes in the stack as its left and right children
            if card in BETNode.OPERATORS:
                temp = BETNode(card)
                temp.add_right(stack.pop())
                temp.add_left(stack.pop())
                stack.append(temp)
        # adds the root node of the created tree to treeset
        treeset.add(stack[0])
    
    # returns the set of all possible binary trees
    return treeset


def find_solutions(cards):
    """ evaluates all potential generated trees and adds it to a set if it all adds up to 24 """
    # cheese sounds like trees so cheese is a list of the trees
    cheese = create_trees(cards)
    solutions = set()
    for tree in cheese:
        if tree.evaluate() == 24:
            solutions.add(tree)
    # if there are no solutions
    if len(solutions) == 0:
        return "no solutions :("
    return solutions