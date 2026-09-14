class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(i, j):
            stack = [(i,j)]
            while stack:
                x, y = stack.pop()
                surrounding = ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))
                for nx, ny in surrounding:
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == '1':
                        stack.append((nx, ny))
                visited[x][y] = True

        ans = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    ans += 1
        return ans

            
