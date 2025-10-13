class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recurse(nums, ans, arr, n): 
            if len(arr) == n: 
                ans.append(arr.copy())
                return
            for i in list(nums):
                if nums[i] == 0:
                    continue
                arr.append(i)
                nums[i] -= 1
                recurse(nums, ans, arr, n)
                nums[i] += 1
                arr.pop()

        ans = []
        arr = []
        freqMap = Counter(nums)
        recurse(freqMap, ans, arr, len(nums))
        return ans
