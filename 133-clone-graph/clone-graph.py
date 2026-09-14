"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        ans = Node(node.val)
        visited[node.val] = ans
        stack = [(node, ans)]
        while stack:
            originalNode, ansNode = stack.pop()
            #print(f'{originalNode.val=}, {ansNode.val=} (should be same)')
            for neighbor in originalNode.neighbors:
                #print(f'{neighbor.val=}')
                if neighbor.val not in visited:
                    temp = Node(neighbor.val)
                    ansNode.neighbors.append(temp)
                    stack.append((neighbor, temp))
                    visited[neighbor.val] = temp
                else:
                    ansNode.neighbors.append(visited[neighbor.val])
        return ans
            