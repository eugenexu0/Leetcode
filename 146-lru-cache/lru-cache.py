class Node:
    def __init__(self, data):
        self.data = data  #(key, val)
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}    #key -> node
        self.head = Node([0, 0]) #most recently used
        self.tail = Node([0, 0]) #least recently used
        # tail -> head
        self.tail.next = self.head
        self.head.prev = self.tail


    def get(self, key: int) -> int:
        #hashmap : key -> val
        if key not in self.map:
            return -1
        #node.prev <- -> node -> <- node.next

        #remove
        node = self.map[key]
        #print(f'{node.data=}')
        #print(f'{node.prev.data=}')
        #print(f'{node.next.data=}')
        node.next.prev = node.prev
        node.prev.next = node.next

        #re-add to "MRU" spot (head)
        self.head.prev.next = node
        node.prev = self.head.prev
        self.head.prev = node
        node.next = self.head
        return node.data[1]


    def put(self, key: int, value: int) -> None:
        #need:
        #track LRU; have some ordering such that
        #LRU is popped when cap is full
        if key not in self.map:
            if self.size == self.capacity:
                #remove from map
                removeKey = self.tail.next.data[0]
                del self.map[removeKey]

                #remove from linkdelist
                removeNode = self.tail.next
                removeNode.next.prev = self.tail
                self.tail.next = removeNode.next
                self.size -= 1

            #add 
            node = Node([key, value])
            #add to linkedlist
            self.head.prev.next = node
            node.prev = self.head.prev
            self.head.prev = node
            node.next = self.head
            #add to map
            self.map[key] = node
            self.size += 1
        else:
            #already in cache:
            #update map, update to MRU
            self.map[key].data[1] = value
            self.get(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)