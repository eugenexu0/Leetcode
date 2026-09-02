# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        if p.val < root.val and root.val < q.val:
            return curr
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(curr.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(curr.right, p, q)
        #if p.val == root.val or q.val == root.val
        #by definition MUST be LCA
        return curr