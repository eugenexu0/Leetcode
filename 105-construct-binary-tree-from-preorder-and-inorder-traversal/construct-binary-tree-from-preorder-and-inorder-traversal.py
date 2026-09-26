# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#preorder = [3,9,20,2,4,15,7], inorder = [2,9,4,3,15,20,7]
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        #print(f'{preorder=}. {inorder=}')
        index = inorder.index(preorder[0])
        #print(f'{index=}')
        leftTree = self.buildTree(preorder[1:], inorder[:index]) if len(preorder) >= 1 else None
        rightTree = self.buildTree(preorder[index + 1:], inorder[index + 1:]) if len(preorder) >= 2 else None
        node = TreeNode(preorder[0], leftTree, rightTree)
        return node