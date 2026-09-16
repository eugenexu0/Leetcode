class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #step 1: count num oranges, find orange
        rows = len(grid)
        cols = len(grid[0])
        numOranges = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    numOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        if numOranges == 0:
            return 0
        ans = -1
        #step 2: go to orange, bfs ("level order traversal")
        while queue:
            #process all rotten oranges for the minute
            tempsize = len(queue)
            for _ in range(tempsize):
                x, y = queue.popleft()
                node = grid[x][y]
                surrounding = ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))
                for ni, nj in surrounding:
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        numOranges -= 1
                        queue.append((ni, nj))
            #minute passes
            ans += 1
        return ans if numOranges == 0 else -1
