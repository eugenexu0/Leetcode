class Solution:
    def trap(self, height: List[int]) -> int:
        #O(n) memory solution
        maxLeft = [height[0]]
        maxRight = [height[-1]]
        for i in range(1, len(height)):
            maxLeft.append(max(maxLeft[i-1],height[i]))

        for i in range(len(height) - 2, -1, -1):
            maxRight.append(max(maxRight[-1],height[i]))
        maxRight.reverse()
        
        water = 0
        left = height[0]
        for i in range(1, len(height) - 1):
            top = min(maxLeft[i-1], maxRight[i+1])
            water = water + max(0, top - height[i])

        return water