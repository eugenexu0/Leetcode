class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = [[math.inf for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                directions = ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1))
                for ni, nj in directions:
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                        dp[i][j] = min(dp[i][j], matrix[i][j] + dp[ni][nj])
        
        return min(dp[-1])