class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            stack = [(i,j)]
            while stack:
                x, y = stack.pop()
                surrounding = ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))
                for nx, ny in surrounding:
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == '1':
                        stack.append((nx, ny))
                visited[x][y] = True

        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    ans += 1
        return ans

            
