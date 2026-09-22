class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [i for i in range(len(edges))]
        rank = [1 for _ in range(len(edges))]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            r1, r2 = find(x), find(y)
            if r1 == r2:
                return False
            if rank[r1] < rank[r2]:
                parent[r1] = r2
            elif rank[r1] > rank[r2]:
                parent[r2] = r1
            else:
                parent[r1] = r2
                rank[r1] += 1
            return True

        for u, v in edges:
            x, y = u - 1, v - 1
            if not union(x, y):
                return [u, v]