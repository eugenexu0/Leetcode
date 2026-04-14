class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 1
        count = 0
        while r < len(nums):
            #iterate thru window
            far = l + nums[l]
            l += 1
            while l < r:
                far = max(far, l + nums[l])
                l += 1
            count += 1
            r = far + 1
        return count