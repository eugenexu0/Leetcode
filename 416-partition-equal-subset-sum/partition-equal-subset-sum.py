class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        ans = False
        @cache
        def dp(n, currSum):
            nonlocal ans
            if currSum == (total / 2):
                ans = True
                return
            if n >= len(nums) or ans or currSum > (total / 2):
                return
            dp(n + 1, currSum + nums[n])
            dp(n + 1, currSum)
        dp(0, 0)
        return ans