# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node: TreeNode, maxInt: int) -> int:
            if not node:
                return 0
            if node.val < maxInt:
                return helper(node.left, maxInt) + helper(node.right, maxInt)
            else:
                return 1 + helper(node.left, node.val) + helper(node.right, node.val)

        if not root:
            return 0
    
        count = 1
        count += helper(root.left, root.val)
        count += helper(root.right, root.val)

        return count
        
