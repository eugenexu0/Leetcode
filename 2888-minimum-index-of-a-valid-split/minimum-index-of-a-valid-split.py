class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        freq = Counter(nums)
        pair = freq.most_common(1)
        dom = pair[0][0]
        domCount = 0
        splitLength = 0
        ans = -1
        for i in range(len(nums)):
            n = nums[i]
            splitLength += 1
            if n == dom:
                domCount += 1
            #print(f'{splitLength=}')
            #print(f'{domCount=}')
            if i == len(nums) - 1 and domCount * 2 <= splitLength:
                return -1
            if ans == -1 and domCount * 2 > splitLength:
                #print("BISDBGOSD")
                ans = i
                domCount = 0
                splitLength = 0
        return ans if ans != len(nums) - 1 else -1