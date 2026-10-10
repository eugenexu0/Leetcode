class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        print(intervals)
        current_end = -math.inf
        ans = 0
        for start, end in intervals:
            if current_end <= start:
                current_end = end
            else:
                ans += 1
        return ans