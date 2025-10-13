class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        down = -1
        downIndex = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                down = nums[i - 1]
                downIndex = i - 1
                break
        if down == -1:
            nums.reverse()
            return
        minimum = inf
        minIndex = -1
        for i in range(len(nums) - 1, downIndex, -1):
            if nums[i] > down and nums[i] < minimum:
                minimum = nums[i]
                minIndex = i

        nums[minIndex], nums[downIndex] = nums[downIndex], nums[minIndex]
        nums[downIndex+1:] = sorted(nums[downIndex + 1:])
        
        