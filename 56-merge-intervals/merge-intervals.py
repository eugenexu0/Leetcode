class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        ans = []
        begin = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if begin <= intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                ans.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
        ans.append([begin, end])
        return ans