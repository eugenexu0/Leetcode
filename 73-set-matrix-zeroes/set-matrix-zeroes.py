class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        turn_row_into_zeroes = [False] * len(matrix)
        turn_col_into_zeroes = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    turn_row_into_zeroes[i] = True
                    turn_col_into_zeroes[j] = True
        for i in range(len(turn_row_into_zeroes)):
            if turn_row_into_zeroes[i]:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(len(turn_col_into_zeroes)):
            if turn_col_into_zeroes[j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        return matrix