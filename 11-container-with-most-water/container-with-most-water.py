class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        h = min(height[i], height[j])
        w = j - i
        maxArea = h * w

        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = h * w

            if area > maxArea:
                maxArea = area

            if (height[i] < height[j]):
                i = i + 1
            else:
                j = j - 1
        return maxArea