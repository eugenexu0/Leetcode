# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 1
        res = -1
        flag = True
        def dfs(node: TreeNode,):
            nonlocal n, k, res, flag
            if not node:
                return -1
            dfs(node.left)
            #print(f'{n=}')
            #print(f'{k=}')
            #print(f'{node.val=}')
            if n == k and flag:
                res = node.val
                flag = False
                return
            else:
                n += 1
            dfs(node.right)
        dfs(root)
        return res
            
            