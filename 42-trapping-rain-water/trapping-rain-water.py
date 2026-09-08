class Solution:
    def trap(self, height: List[int]) -> int:
        #key obv: formula for water in a position is:
        #min(tallest height left, tallest height right) - current height @ pos
        left, right = 0, len(height) - 1
        maxleft, maxright = height[left], height[right]
        ans = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                ans += max(maxleft - height[left], 0)
                maxleft = max(maxleft, height[left])
            else:
                right -= 1
                ans += max(maxright - height[right], 0)
                maxright = max(maxright, height[right])
        return ans