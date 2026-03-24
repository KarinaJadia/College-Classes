class heapin:
    ''' wrapper heap class '''
    def __init__(self):
        self._entries = []
       
    def _parent(self, i):
        '''returns the parent of the heap(i)'''
        return (i - 1) // 2
    
    def _pop(self):
        '''removes and returns the smallest item from the heap'''
        L = self._entries
        last_elem_index = len(L) - 1
        self._swap(0, last_elem_index)
        smallest = L.pop()
        self._downheap(0)
        return smallest

    def _children(self, i):
        '''returns the children of heap(i)'''
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))
   
    def _swap(self, a, b):
        '''swaps list positions from self._entries'''
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        '''maintains the min-heap property upwards'''
        L = self._entries
        parent = self._parent(i)
        if 0 <= i < len(L):
            parent = self._parent(i)
            if i > 0 and L[i] < L[parent]:
                self._swap(i, parent)
                self._upheap(parent)

    def _downheap(self, i):
        '''maintains the min-heap property downwards'''
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                    self._swap(i, child)
                    self._downheap(child)