from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        """creates a tiny linked list, tests if a number is in it, removes said number, then tests again"""
        tL = DLL([1,2,3])
        assert 1 in tL # should be true
        tL.remove_first()
        assert not 1 in tL # now should be false
        tL.add_last(1)
        assert 1 in tL # should be true again

    def test_neighbors(self):
        tL = DLL([1,2,3])
        assert tL.neighbors(1) == (None, 2) # true
        assert tL.neighbors(2) == (1, 3) # true
        assert tL.neighbors(3) == (2, None) # true
        # testing if a runtime error is raised when I try to remove an item that does not exist
        with self.assertRaises(RuntimeError):
            tL.neighbors(4) # should raise an error

    def test_remove_item(self):
        tL = DLL([1,2,3,4,5])

        assert 3 in tL
        assert len(tL) == 5

        # removing from the middle
        tL.remove_node(3)
        assert 3 not in tL
        assert len(tL) == 4
        assert tL.neighbors(2) == (1, 4) # since 3 is removed, 2's neighbors should be 1 and 4

        # removing the head
        tL.remove_node(1)
        assert 1 not in tL
        assert tL.neighbors(2) == (None, 4)
        
        # trying to remove an element that doesn't exist
        with self.assertRaises(RuntimeError):
            tL.neighbors(6) # should raise an error

unittest.main()