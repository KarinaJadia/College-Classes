from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                assert puzzle.solve_puzzle([1,2,3,1,0], 'cw') == True

        def testCounterClockwise(self):
                assert puzzle.solve_puzzle([1,3,2,1], 'ccw') == True

        def testMixed(self):
                assert puzzle([3, 6, 4, 1, 3, 4, 2, 0]) == True
        
        def testUnsolveable(self):
                assert puzzle([3, 4, 1, 2, 0]) == False

unittest.main()