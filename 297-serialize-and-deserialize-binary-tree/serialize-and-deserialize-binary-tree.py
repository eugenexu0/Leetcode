# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        i = 0
        values = data.split(",")
        root = TreeNode(values[0])
        queue = deque([root])

        while queue:
            node = queue.popleft()
            i += 1
            if i < len(values):
                left = values[i]
                if left != "#":
                    node.left = TreeNode(int(left))
                    queue.append(node.left)
            i += 1
            if i < len(values):
                right = values[i]
                if right != "#":
                    node.right = TreeNode(int(right))
                    queue.append(node.right)

        return root

            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))