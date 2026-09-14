class Solution:

    def __init__(self, w: List[int]):
        self.prefixsum = []
        tempsum = 0
        for n in w:
            tempsum += n
            self.prefixsum.append(tempsum)
        #print(f'{self.prefixsum=}')

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefixsum[-1])
        left, right = 0, len(self.prefixsum) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.prefixsum[mid] == target:
                return mid
            elif self.prefixsum[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
# [2, 5, 3, 1, 4]
# sum = 15
# [2, 7, 10, 11, 15]
# 1 - 15
# 4

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()