"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        ans = Node(head.val)

        #construct linkedlist without random
        curr = ans
        hashmap = {head : curr}
        headptr = head.next
        while headptr:
            nextNode = Node(headptr.val)
            curr.next = nextNode
            curr = nextNode
            hashmap[headptr] = curr
            headptr = headptr.next

        #assign random
        curr = ans
        while head:
            if head.random:
                curr.random = hashmap[head.random]
            head = head.next
            curr = curr.next
        
        return ans

