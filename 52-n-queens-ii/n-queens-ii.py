      
class Solution:
    def recurseQueens(self, answers: List[int], board: List[str], numQueens: int, n: int):
        def isValid(board: List[str], i: int, j: int) -> bool:
            #n x n
            for x in range(len(board)):
                for y in range(len(board)):
                    if board[x][y] == "Q":
                        if x == i or y == j:
                            return False
                        if abs(x - i) == abs(y - j):
                            return False
            return True
        #if we placed all our queens, add it to our answers
        if (numQueens == n):
            answers[0] += 1
            return            
        
        #go through a row and try placing queens
        for i in range(len(board)):
            if (isValid(board, numQueens, i)):
                board[numQueens] = board[numQueens][:i] + 'Q' + board[numQueens][i+1:]
                self.recurseQueens(answers, board, numQueens + 1, n)
                #after placing queen, remove it to check for possible
                #other queen possibilities in other rows
                board[numQueens] = board[numQueens][:i] + '.' + board[numQueens][i+1:]
        
        #if we can't place any queens, solution is impossible
        
        
        
    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [("." * n) for _ in range(n)]
        ans = [0]
        self.recurseQueens(ans, board, 0, n)
        return ans[0]