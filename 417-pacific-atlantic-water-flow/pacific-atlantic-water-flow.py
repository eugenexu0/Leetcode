class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ans = []
        rows, cols = len(heights), len(heights[0])
        canReachPacific = [[True if i == 0 or j == 0 else False for i in range(cols)] for j in range(rows)]
        canReachAtlantic = [[True if i == cols - 1  or j == rows - 1 else False for i in range(cols)] for j in range(rows)]
        def dfs(starts, isPacific):
            
            stack = starts[:]
            #print(f'{stack=}')
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            for i, j in stack:
                visited[i][j] = True
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

        pacificStarts = []
        atlanticStarts = []
        for i in range(rows):
            pacificStarts.append((i, 0))
            atlanticStarts.append((i, cols - 1))
        for j in range(cols):
            pacificStarts.append((0, j))
            atlanticStarts.append((rows - 1, j))
        dfs(pacificStarts, True)
        dfs(atlanticStarts, False)
        #print(f'{canReachPacific=}, {canReachAtlantic=}')
        return [[i, j] for i in range(rows) for j in range(cols) if canReachPacific[i][j] and canReachAtlantic[i][j]]