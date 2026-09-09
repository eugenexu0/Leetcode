# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        ans = ListNode(node.val)
        newList = ans
        node = node.next
        while node:
            old = None
            while newList and node.val > newList.val:
                old = newList
                newList = newList.next
            temp = ListNode(node.val)
            temp.next = newList
            if not old:
                ans = temp
            else:
                old.next = temp
            node = node.next
            newList = ans
        return ans