from hw3 import *
import unittest

class test_find_pairs(unittest.TestCase):
    # testing find_pairs_naive()
    def test_fpn(self):
        assert (find_pairs_naive([1, 2, 3, 4, 5], 5)) == ([1, 4], [2, 3]) # true
        assert (find_pairs_naive([1, 2, 3, 4, 5], 6)) == ([1, 5], [2, 4]) # true
        assert (find_pairs_naive([], 10)) == () # true
        assert (find_pairs_naive([1, 2, 3], 10)) == () # true

    # testing find_pairs_optimized()
    def test_fpo(self):
        assert(find_pairs_optimized([1,2,3,4,5], 5)) == ([3, 2], [4, 1]) # true
        assert(find_pairs_optimized([1,2,3,4,5], 6)) == ([4, 2], [5, 1]) # true
        assert(find_pairs_optimized([], 10)) == () # true
        assert (find_pairs_optimized([1, 2, 3], 10)) == () # true

unittest.main() 