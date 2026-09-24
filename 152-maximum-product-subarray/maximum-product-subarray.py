class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        lowest, highest = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            lowest, highest = min(val, lowest * val, highest * val), max(val, lowest * val, highest * val)
            ans = max(ans, highest)
        return ans