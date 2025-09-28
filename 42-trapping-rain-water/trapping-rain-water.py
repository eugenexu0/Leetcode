class Solution:
    def trap(self, height: List[int]) -> int:
        #O(1) memory sol
        leftPtr = 0
        rightPtr = len(height) - 1
        maxLeft = height[0]
        maxRight = height[-1]
        water = 0
        while (leftPtr < rightPtr):
            if height[leftPtr] < height[rightPtr]:
                leftPtr = leftPtr + 1
                maxLeft = max(maxLeft, height[leftPtr])
                water = water + max(0, maxLeft - height[leftPtr])
            else:
                rightPtr = rightPtr - 1
                maxRight = max(maxRight, height[rightPtr])
                water = water + max(0, maxRight - height[rightPtr])
        return water

            