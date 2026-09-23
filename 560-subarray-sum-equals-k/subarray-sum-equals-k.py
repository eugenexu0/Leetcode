class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        seen = defaultdict(int)
        seen[0] = 1
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] + nums[i]
            if (prefix[i] - k) in seen:
                ans += seen[prefix[i] - k]
            seen[prefix[i]] += 1
        return ans
