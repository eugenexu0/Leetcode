class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) * len(matrix[0]) - 1
        #print(f'low {low} high {high}')
        while low <= high:
            mid = (low + high) // 2
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])
            #print(f'{i} {j}')
            val = matrix[i][j]
            if val == target:
                return True
            elif val > target:
                high = mid - 1
            elif val < target:
                low = mid + 1
        return False