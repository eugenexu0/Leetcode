class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, len(colors) - 1
        ans = -1
        while l != r:
            if colors[l] != colors[r]:
                ans = max(ans, r - l)
            l += 1
        l = 0
        while l != r:
            if colors[l] != colors[r]:
                ans = max(ans, r - l)
            r -= 1
        return ans