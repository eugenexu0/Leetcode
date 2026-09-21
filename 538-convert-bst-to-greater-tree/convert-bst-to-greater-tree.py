# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root, total) -> int:
            if not root:
                return total
            root.val += dfs(root.right, total)
            return dfs(root.left, root.val)
        dfs(root, 0)
        return root