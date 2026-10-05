class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = nums[:]
        def backtrack(index):
            if index == len(nums):
                ans.append(perm[:])
            for i in range(index, len(nums)):
                perm[index], perm[i] = perm[i], perm[index]
                backtrack(index + 1)
                perm[index], perm[i] = perm[i], perm[index]
        backtrack(0)
        return ans