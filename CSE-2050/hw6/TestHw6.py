import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted
from Samesies import samesies

# TODO: implement tests for sort_halfsorted

class Test_SortHalfSorted(unittest.TestCase):
   def test_halfsorted_bubble(self):
      # alt tests without halfsorted
      """ creates lists with different sizes and 0 placements and sorts """
      """ this one fails but I for the life of me cannot figure out what I am doing wrong """
      for n in range(10, 50):
         for i in range(1, n-1):
            # generated a half-sorted list of size i
            L, index = generate_halfsorted(n, i)
            og = L[:]
            bubble(L, 0, len(L)-1)
            assert(is_sorted(L)) # checks if it's sorted
            assert(samesies(og, L)) # makes sure they have the same elements
      

   def test_halfosrted_selection(self):
      """creates lists up to length 60 with the 0 in all possible places and different types of lists and tests if it's sorted"""
      for pattern in ['random', 'reverse', 'sorted']:
         for n in range(60):
            for i in range(n):
               L, index = generate_halfsorted(n, i, pattern)
               # deep-copied list
               L2 = L[:]
               sort_halfsorted(L, selection)
               assert is_sorted(L)
               # samesies is the function I created that checks if the lists still have the same elements
               assert samesies(L, L2)
      

   def test_halfsorted_insertion(self):
      # alt tests without halfsorted
      """ creates lists with different sizes and 0 placements and sorts """
      for pattern in ['random', 'reverse', 'sorted']:
         for n in range(10, 50):
            for i in range(1, n-1):
               # generated a half-sorted list of size i
               Li = generate_halfsorted(n, i)[0]
               og = Li[:]
               insertion(Li, 0, len(Li)-1)
               assert(is_sorted(Li)) # checks if it's sorted
               assert(samesies(og, Li)) # makes sure they have the same elements


# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()