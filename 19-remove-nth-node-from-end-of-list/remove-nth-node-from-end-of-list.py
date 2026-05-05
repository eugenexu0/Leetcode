# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        i = 0
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1
        
        #case if remove first node
        if i == n:
            head = head.next
            return head

        #slow is now at one place before "n"
        nextn = None
        if slow.next and slow.next.next:
            nextn = slow.next.next
        slow.next = nextn
        return head