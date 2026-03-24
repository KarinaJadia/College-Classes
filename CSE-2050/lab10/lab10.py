class Entry:
    def __init__ (self, item, priority):
        self.priority = priority
        self.item = item
    
    def __lt__ (self, other):
        return self.priority < other.priority
    
    def __eq__ (self, other):
        return self.priority == other.priority and self.item == other.item

class PQ_UL(Entry):
    def __init__ (self):
        self._entries = []
            
    def __len__ (self):
        return len(self._entries)
    
    def insert (self, item, priority):
        self._entries.append(Entry(item, priority))

    def find_min (self):
        if len(self._entries) == 0:
            return 'No entries found'
        low = self._entries[0]
        for item in self._entries:
            if item < low:
                low = item
        return low
    
    def remove_min (self):
        remove = self.find_min()
        self._entries.remove(remove)
        return remove
    
class PQ_OL(Entry):
    def __init__ (self):
        self._entries = []

    def __len__ (self):
        return len(self._entries)

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._entries.sort()

    def find_min(self):
        return self._entries[0]
    
    def remove_min(self):
        L = self._entries
        remove = L[0]
        L[0] = L[-1]

        L.pop()
        L.sort()
        return remove