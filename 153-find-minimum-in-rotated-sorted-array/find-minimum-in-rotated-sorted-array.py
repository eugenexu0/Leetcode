class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            #print(f'low {low} mid {mid} high {high}')
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[0]