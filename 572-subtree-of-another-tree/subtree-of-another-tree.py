# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root and not root2:
                return True
            if (root and not root2) or (not root and root2):
                return False
            return root.val == root2.val and isSameTree(root.left, root2.left) and isSameTree(root.right, root2.right)
        
        ans = False
        def dfs(root: Optional[TreeNode], subroot: Optional[TreeNode]):
            nonlocal ans
            if not root:
                return
            if isSameTree(root, subroot):
                ans = True
                return
            dfs(root.left, subroot)
            dfs(root.right, subroot)
        dfs(root, subRoot)
        return ans