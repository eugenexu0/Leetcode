class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        freqList = Counter(nums)
        for n in nums:
            if freqList[n] == 0:
                continue
            for i in range(k):
                if n + i not in freqList or freqList[n + i] == 0:
                    return False
                freqList[n + i] -= 1

        return True