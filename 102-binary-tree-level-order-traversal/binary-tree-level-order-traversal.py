# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        levelq = deque([root])
        ans.append([root.val])
        #need to loop
        while levelq:
            level = []
            tempq = []
            while levelq:
                node = levelq.popleft()
                if node.left:
                    level.append(node.left.val)
                    tempq.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    tempq.append(node.right)
            #print(f'{level=}')
            if level:
                ans.append(level)
            levelq.extend(tempq)
        #print(f'{ans=}')
        return ans

        