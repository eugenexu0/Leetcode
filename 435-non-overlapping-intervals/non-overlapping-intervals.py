class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        current_end = -math.inf
        ans = 0
        for start, end in intervals:
            if current_end <= start:
                current_end = end
            elif current_end > end:
                current_end = end
                ans += 1
            else:
                ans += 1
        return ans