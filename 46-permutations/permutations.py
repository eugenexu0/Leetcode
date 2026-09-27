class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def backtrack(n, temparr):
            if n == len(nums) - 1:
                ans.append(temparr[:])
                return
            
            for i in range(n, len(nums)):
                temparr[i], temparr[n] = temparr[n], temparr[i]
                backtrack(n + 1, temparr)
                temparr[i], temparr[n] = temparr[n], temparr[i]
        backtrack(0, nums)
        return ans
            
        #1, 2, 3
        # n = 0, i = 1 1, 2, 3 ->2, 1, 3 
        # n = 1, i = 2 2, 1, 3 -> 2, 3, 1
        # n = 1, i = 2 2, 1, 3 -> 2, 1, 3

        # n = 0, i = 1 1, 2, 3 -> 1, 3, 2
        # n = 1, i = 2 1, 3, 2 => 1, 2, 3
