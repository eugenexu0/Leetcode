# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Thank you amy shi for your kind pateince
        #with silly old me
        # i shudve believed u...
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr)
            ptr = ptr.next

        i, j = 0, len(arr) - 1
        while i < j:
            if i != 0:
                arr[j+1].next = arr[i]
            arr[i].next = arr[j]
            i += 1
            j -= 1
        if i == j and len(arr) % 2 == 1 and len(arr) > 1:
            arr[i+1].next = arr[i]
        arr[i].next = None
        return head