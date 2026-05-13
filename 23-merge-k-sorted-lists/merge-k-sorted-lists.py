# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        counter = 0
        for node in lists:
            #counter to take care of ties
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        
        if heap:
            val, _, node = heapq.heappop(heap)
            ans = ListNode(val, None)
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        
        else:
            ans = None

        #print(ans)
        ptr = ans
        while heap:
            #print(heap)
            val, _, node = heapq.heappop(heap)
            nextnode = ListNode(val, None)
            ptr.next = nextnode
            ptr = ptr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        
        return ans
        