class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [[0] * n for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        position = 1
        while (position <= n*n):
            #top row
            for i in range(left, right):
                arr[top][i] = position
                position += 1
            top += 1
            
            #right column
            for i in range(top, bottom):
                arr[i][right-1] = position
                position += 1
            right -= 1

            #bottom row
            for i in range(right-1, left-1, -1):
                arr[bottom-1][i] = position
                position += 1
            bottom -= 1

            #left column
            for i in range(bottom-1, top-1, -1):
                arr[i][left] = position
                position += 1
            left += 1
        return arr
