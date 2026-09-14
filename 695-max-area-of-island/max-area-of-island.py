class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(i, j):
            #print(f'searching {i=}, {j=}')
            queue = deque([[i, j]])
            area = 1
            while queue:
                i, j = queue.popleft()
                surrounding = ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))
                for ni, nj in surrounding:
                    if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj] and grid[ni][nj] == 1:
                        visited[ni][nj] = True
                        queue.append([ni, nj])
                        area += 1
            #print(f'{area=}')
            return area
        ans = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                node = grid[i][j]
                if node == 1 and not visited[i][j]:
                    visited[i][j] = True
                    ans = max(ans, bfs(i, j))
        return ans
            