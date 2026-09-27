class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.oldest = Node(0,0)
        self.latest = Node(0,0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def remove(self, node) -> None:
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node) -> None:
        prv, nxt = self.latest.prev, self.latest
        prv.next = nxt.prev = node
        node.prev = prv
        node.next = nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]
