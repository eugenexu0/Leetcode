# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        #was p OR q found?
        def dfs(root) -> bool:
            nonlocal ans
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                ans = root
            if root == p:
                if left or right:
                    ans = root
                return True
            if root == q:
                if left or right:
                    ans = root
                return True
            return left or right
        dfs(root)
        return ans
        