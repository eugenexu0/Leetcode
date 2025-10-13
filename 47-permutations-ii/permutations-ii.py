class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recurse(nums, ans, arr, n): 
            if len(arr) == n: 
                if not arr in ans:
                    ans.append(arr)
                return
            for i in nums:
                newarr = arr.copy()
                newarr.append(i)
                newnums = nums.copy()
                newnums.remove(i)
                recurse(newnums, ans, newarr, n)

        ans = []
        arr = []
        recurse(nums, ans, arr, len(nums))
        return ans
