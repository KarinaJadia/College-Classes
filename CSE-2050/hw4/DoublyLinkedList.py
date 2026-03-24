# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head

        """ I think this is what you want? I created a new dictionary and did item: node then added the old dictionary
        to the end then updated the main _nodes dictionary (I can't figure out an easier way to add to the front of a
        dictionary if there is one)"""
        newDict = {item: self._tail}
        newDict.update(self._nodes)
        self._nodes = newDict


    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        
        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail

        """adds the item:node to the end of the dictionary"""
        self._nodes.update({item:self._tail})

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None
        
        """deletes specific key that was removed from list"""
        del self._nodes[item]

        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        """deletes specific item that was removed from list"""
        del self._nodes[item]

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        """checks if item is in dictionary and returns true if it is, false if it isn't"""
        return item in self._nodes

        # I put my old code here in case the thing didn't work
        """current_node = self._head
        while current_node:
            if current_node.item == item:
                return True
            current_node = current_node._next
        return False"""

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        """goes through list for item, then returns previous and next on the list"""
        current_node = self._head
        prev_item = None
        next_item = None

        # for if the item is not in the list
        if item not in self._nodes:
            raise RuntimeError
        
        # iterates through list looking for item
        while current_node:
            if current_node.item == item:
                if current_node._next:
                    next_item = current_node._next.item
                if prev_item:
                    return (prev_item, next_item)
                else:
                    return (None, next_item)
            else:
                prev_item = current_node.item
                current_node = current_node._next

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        """removes item from list and dictionary, then updates head and tail of previous and next and length"""
        # for if the item is not in the list
        if item not in self._nodes:
            raise RuntimeError
        
        # updates length of list
        self._len -= 1

        # deleting from the actual list
        main = self._head
        for i in range(0, self._len):
            if main.item == item:
                # my code works 
                if main._prev == None:
                    self._head = main._next
                elif main._next == None:
                    self._tail = main._prev
                else:
                    main._prev._next = main._next
                    main._next._prev = main._prev
            else:
                main = main._next

        # deletes from dictionary
        del self._nodes[item]