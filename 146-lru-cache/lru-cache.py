class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        #"next" points to RIGHT node
        self.least, self.most = Node(0, 0), Node(0, 0)
        #these two head/tail are "dummy" pointers
        #least.next represents least used node
        #most.prev represents most used node
        self.least.next = self.most
        self.most.prev = self.least

    def remove(self, node: Node):
        #remove a node from the list
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node: Node):
        #insert a node to the right of list
        node.next = self.most
        node.prev = self.most.prev
        self.most.prev.next = node
        self.most.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            #reorder to put node in most used
            self.remove(self.map[key])
            self.insert(self.map[key])
            #return value
            return self.map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self.insert(node)
        if len(self.map) > self.cap:
            removed = self.least.next
            self.remove(removed)
            del self.map[removed.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)