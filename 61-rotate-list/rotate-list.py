# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        slow, fast = head, head
        count = 1
        while fast.next:
            fast = fast.next
            count += 1
        n = k % count
        if n == 0:
            return head
        for i in range(count - n - 1):
            slow = slow.next
        start = slow.next
        slow.next = None
        fast.next = head
        return start
