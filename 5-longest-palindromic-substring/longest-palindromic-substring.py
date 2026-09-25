class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        anslen = 0
        #odd
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > anslen:
                    ans = s[l:r+1]
                    anslen = r - l + 1
                l -= 1
                r += 1
        #even
        for i in range(1, len(s)):
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > anslen:
                    ans = s[l:r+1]
                    anslen = r - l + 1
                l -= 1
                r += 1
        return ans