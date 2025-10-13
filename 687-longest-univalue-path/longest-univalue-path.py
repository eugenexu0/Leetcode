# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(root):
            if not root:
                return 0

            #dfs left, right
            leftPath = dfs(root.left)
            rightPath = dfs(root.right)

            #if left / right child node matches, add 1
            #if it doesn't, it's not worth anything
            #ex: if child node is 3 and our cur "streak" is 4
            #then that leftPath is gonna return the longest path for 3s, not 4
            #so it's worthless to us
            if root.left and root.val == root.left.val:
                leftPath += 1
            else:
                leftPath = 0
            if root.right and root.val == root.right.val:
                rightPath += 1 
            else:
                rightPath = 0
            #global var to keep track of longest we've seen
            #leftPath + rightPath is 1 long path thru our root
            self.longest = max(self.longest, leftPath + rightPath)
            #now for root, decide if we want to continue along left or right chain
            return max(leftPath, rightPath)
        dfs(root)
        return self.longest