class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * (len(nums) - 1)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        dp2 = [0] * len(nums)
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            dp2[i + 1] = max(dp2[i], dp2[i - 1] + nums[i + 1])
        return max(dp[-1], dp2[-1])

