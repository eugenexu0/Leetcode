class Solution:

    def __init__(self, w: List[int]):
        self.nums = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        tempsum = 0
        for i, n in enumerate(self.nums):
            tempsum += n
            if tempsum >= rand:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()