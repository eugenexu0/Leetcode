class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ans = []
        rows, cols = len(heights), len(heights[0])
        canReachPacific = [[True if i == 0 or j == 0 else False for i in range(cols)] for j in range(rows)]
        canReachAtlantic = [[True if i == cols - 1  or j == rows - 1 else False for i in range(cols)] for j in range(rows)]
        def dfs(i, j, isPacific):
            #print(f'{canReachPacific=}, {canReachAtlantic=}')
            stack = [(i, j)]
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            while stack:
                x, y = stack.pop()
                node = heights[x][y]
                surrounding = ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))
                for ni, nj in surrounding:
                    if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj] and heights[ni][nj] >= node:
                        stack.append((ni, nj))
                        visited[ni][nj] = True
                        if isPacific:
                            canReachPacific[ni][nj] = True
                        else:
                            canReachAtlantic[ni][nj] = True

        for i in range(rows):
            dfs(i, 0, True)
            dfs(i, cols - 1, False)
        for j in range(cols):
            dfs(0, j, True)
            dfs(rows - 1, j, False)
        return [[i, j] for i in range(rows) for j in range(cols) if canReachPacific[i][j] and canReachAtlantic[i][j]]