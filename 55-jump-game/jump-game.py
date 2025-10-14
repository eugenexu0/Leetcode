class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpLocation = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= jumpLocation:
                jumpLocation = i
        return jumpLocation == 0
