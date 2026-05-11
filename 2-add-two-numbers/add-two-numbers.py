# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        ptr = ans
        total = 0
        while l1 or l2:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            ptr.val = total % 10
            carry = total // 10
            total = carry
            if l1 or l2:
                ptr.next = ListNode(0, None)
                ptr = ptr.next
        if total != 0:
            ptr.next = ListNode(total, None)
        return ans