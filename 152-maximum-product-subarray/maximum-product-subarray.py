class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp = [(math.inf, -math.inf)] * len(nums) #pair of (lowest, highest)
        dp[0] = (nums[0], nums[0])
        ans = nums[0]
        for i in range(1, len(nums)):
            lowest, highest = dp[i - 1]
            val = nums[i]
            dp[i] = (min(val, lowest * val, highest * val), max(val, lowest * val, highest * val))
            ans = max(ans, dp[i][1])
        return ans