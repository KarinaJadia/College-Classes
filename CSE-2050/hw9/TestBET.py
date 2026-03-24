import unittest
from BET import BETNode, create_trees, find_solutions

class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        # answer should be -5
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))

        self.assertEqual(repr(root), '(A*(2-(3+4)))')
        self.assertEqual(root.evaluate(),-5)


    def test_evaluate_tree1(self):
        r""" string representation
                    +
                   / \
                  4   *
                     / \
                    -   7
                   / \
                  K   5
        """
        # answer should be 60
        root = BETNode('+')
        root.add_left(BETNode('4'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('-'))
        root.right.add_right(BETNode('7'))
        root.right.left.add_left(BETNode('K'))
        root.right.left.add_right(BETNode('5'))

        self.assertEqual(repr(root),'(4+((K-5)*7))')
        self.assertEqual(root.evaluate(),60)


    def test_evaluate_tree2(self):
        # evaluates the edge case where a number is divided by zero
        r""" string representation
                *
               / \
              -   6
             / \
            3   /
               / \
              6   0
        """
        root = BETNode('*')
        root.add_left(BETNode('-'))
        root.add_right(BETNode('6'))
        root.left.add_left(BETNode('3'))
        root.left.add_right(BETNode('/'))
        root.left.right.add_left(BETNode('6'))
        root.left.right.add_right(BETNode('0'))

        self.assertEqual(repr(root),'((3-(6/0))*6)')
        # whole expression should return infinity
        self.assertEqual(root.evaluate(),-float('inf'))

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        ''' testing trees with no duplicates, should total to 7680'''
        trees = create_trees(['1','3','4','6'])
        self.assertEqual(len(trees),7680)
        
    def test_hand2(self):
        ''' testing trees with duplicates, should total to 3840 '''
        trees = create_trees(['1','3','4','4'])
        self.assertEqual(len(trees),3840)
        

class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        ''' tests small unsolvable tree and makes sure solved is the string of no solutions '''
        solved = find_solutions(['A','A','2','3'])
        self.assertEqual(solved, "no solutions :(")

    def test_A23Q(self):
        ''' makes all possible trees with A, 2, 3, and Q and tests that each solution works '''
        solved = find_solutions(['A','2','3','Q'])
        for tree in solved:
            self.assertEqual(tree.evaluate(), 24)
        
unittest.main()