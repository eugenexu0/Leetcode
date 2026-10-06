# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        #ans = max path from left, right
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return (0, False)
            left, leftfound = dfs(root.left)
            right, rightfound = dfs(root.right)
            #found infected
            if root.val == start:
                ans = max(ans, max(left, right))
                return (1, True)
            elif leftfound:
                ans = max(ans, left + right)
                return (1 + left, True)
            elif rightfound:
                ans = max(ans, left + right)
                return (1 + right, True)
            return (1 + max(left, right), False)
        dfs(root)
        return ans