class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def distance(i: int, j: int, k: int) -> int:
            return abs(i - j) + abs(j - k) + abs(k - i)
        seen = {}
        for i, n in enumerate(nums):
            if not n in seen:
                seen[n] = [i]
            else:
                seen[n].append(i)
        ans = math.inf
        for key, val in seen.items():
            if len(val) >= 3:
                l, r = 0, 2
                while r < len(val):
                    ans = min(ans, distance(val[l], val[l+1], val[r]))
                    l += 1
                    r += 1
        return -1 if ans == math.inf else ans