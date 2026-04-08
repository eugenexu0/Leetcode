class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            idx, r = q[0], q[1]
            while idx <= r:
                nums[idx] = (nums[idx] * q[3]) % (10**9 + 7)
                idx += q[2]

        res = nums[0]
        for n in range(1, len(nums)):
            res = res ^ nums[n]
        return res
