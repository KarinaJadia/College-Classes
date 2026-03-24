import unittest
import random
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort, is_sorted


class Test_linear_scan(unittest.TestCase):
    """ this one works """
    # tests that a sorted list will be the number for linear
    assert linear_scan([1,2,3,4,5]) == 0

    # tests that a reverse sorted list will the number for reverse
    assert linear_scan([5,4,3,2,1]) == 4

    # tests that it knows there are 3 unsorted elements (meaning elements that are larger than the element next to them)
    assert linear_scan([1,4,2,5,3,7,6]) == 3 # (4, 5, 7 are unsorted)

class Test_reverse_list(unittest.TestCase):
    """ this one works """
    # tests that a reverse sorted list will become unreverse sorted
    lis = [5,4,3,2,1]
    reverse_list(lis)
    assert is_sorted(lis)

class Test_insertionsort(unittest.TestCase):
    """ this one works """
    # tests that a list will sort
    lst = [12,321,53,25,4352,32,432,2,643,3,32,243]
    insertionsort(lst, 0, len(lst))
    assert is_sorted(lst)

    # tests randomly generated list
    lstsss = [random.randint(1, 20) for i in range(15)]
    insertionsort(lstsss)
    assert is_sorted(lstsss)

class Test_quicksort(unittest.TestCase):
    """ quicksort """
    # tests that a list will sort
    lst = [12,321,53,25,4352,32,432,2,643,3,32,243]
    quicksort(lst)
    assert is_sorted(lst)

    # tests randomly generated list
    lstss = [random.randint(1, 20) for i in range(15)]
    quicksort(lstss)
    assert is_sorted(lstss)

class Test_mergesort(unittest.TestCase):
    """ tests if merge sort sorts """
    # tests list
    lst = [12,321,53,25,4352,32,432,2,643,3,32,243]
    mergesort(lst)
    assert is_sorted(lst)

    # tests randomly generated list
    lsts = [random.randint(1, 20) for i in range(15)]
    mergesort(lsts)
    assert is_sorted(lsts)

class Test_magicsort(unittest.TestCase):
    """tests if magic sort returns the sorting algorithms used and actually sorts"""
    # tests reverse list
    lis = [5,4,3,2,1]
    x = magic_sort(lis)
    assert is_sorted(lis)
    assert x == {'reverse_list'}

    # tests linear (I don't think this is required but I built magic sort with linear first and I don't want to remove it)
    li = [1,2,3,4,5,6]
    y = magic_sort(li)
    assert y == {'linear'}

    # tests insertion sort
    ls = [1,4,2,5]
    z = magic_sort(ls)
    assert is_sorted(ls)
    assert z == {'insertionsort'}

    # tests quicksort
    theL = [random.randint(1, 20) for i in range(15)]
    w = magic_sort(theL)
    assert is_sorted(theL)
    assert w == {'quicksort', 'insertionsort'}



unittest.main()