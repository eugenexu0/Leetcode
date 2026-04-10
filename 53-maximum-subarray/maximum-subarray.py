class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, high = 0, -math.inf
        for n in nums:
            total += n
            high = max(total, high)
            if total < 0:
                total = 0
        return high