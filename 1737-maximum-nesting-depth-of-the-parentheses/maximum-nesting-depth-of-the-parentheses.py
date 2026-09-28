class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        ans = 0
        for c in s:
            if c == "(":
                depth += 1
            if c == ")":
                depth -= 1
            ans = max(ans, depth)
        return ans