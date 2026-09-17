class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #go through edge of board, DFS for each O on the edge
        #and mark as "cannot capture"
        rows, cols = len(board), len(board[0])
        cannotCapture = [[False for j in range(cols)] for i in range(rows)]
        stack = []
        for i in range(rows):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][cols - 1] == "O":
                stack.append((i, cols - 1))
        for j in range(cols):
            if board[0][j] == "O":
                stack.append((0, j))
            if board[rows - 1][j] == "O":
                stack.append((rows - 1, j))
            
        for i, j in stack:
            cannotCapture[i][j] = True
        while stack:
            i, j = stack.pop()
            surrounding = ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))
            for ni, nj in surrounding:
                if 0 <= ni < rows and 0 <= nj < cols and not cannotCapture[ni][nj] and board[ni][nj] == "O":
                    stack.append((ni, nj))
                    cannotCapture[ni][nj] = True
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and not cannotCapture[i][j]:
                    board[i][j] = "X"
