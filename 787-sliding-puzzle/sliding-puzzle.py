import math

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        visited = {}
        ans = math.inf

        def dfs(board, opcount):
            nonlocal ans
            #print(f'{board=}, {opcount=}')
            if board == [[1,2,3],[4,5,0]]:
                ans = min(ans, opcount)
                print(ans)
                return
            
            boardstring = "".join("".join(map(str, row)) for row in board)
            visited[boardstring] = opcount

            ni, nj = 0, 0
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        ni = i
                        nj = j

            surrounding = ((ni + 1, nj), (ni, nj + 1), (ni - 1, nj), (ni, nj - 1))

            for i, j in surrounding:
                if 0 <= i < 2 and 0 <= j < 3:
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    boardstring = "".join("".join(map(str, row)) for row in board)
                    if boardstring not in visited or opcount < visited[boardstring]:
                        dfs(board, opcount + 1)
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

        dfs(board, 0)
        return -1 if ans == math.inf else ans
            
