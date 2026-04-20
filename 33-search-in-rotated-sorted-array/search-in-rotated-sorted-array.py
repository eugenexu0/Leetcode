class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            #print(f'{low} {mid} {high}')
            if nums[mid] == target:
                return mid
            #partition reset is on RIGHT side
            #LEFT is sorted
            if nums[mid] > nums[high]:
                #check if target is on left or right:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            #RIGHT is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1