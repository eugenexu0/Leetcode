class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        seen = defaultdict(int)
        seen[0] = 1
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                curr = nums[i]
            else:
                curr += nums[i]
            ans += seen[curr - k]
            seen[curr] += 1
        return ans
