class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            #print(f'searching {i=}, {j=}')
            queue = deque([[i, j]])
            area = 1
            while queue:
                i, j = queue.popleft()
                node = grid[i][j]
                surrounding = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
                for ni, nj in surrounding:
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not visited[ni][nj] and grid[ni][nj] == 1:
                        visited[ni][nj] = True
                        queue.append([ni, nj])
                        area += 1
            #print(f'{area=}')
            return area
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = grid[i][j]
                if node == 1 and not visited[i][j]:
                    visited[i][j] = True
                    ans = max(ans, bfs(i, j))
        return ans
            