class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""
        maxLen = 1
        leftSol = rightSol = 0
        for i in range(0, len(s)):
            #odd
            left = i-1
            right = i+1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > maxLen):
                    maxLen = right - left + 1
                    leftSol, rightSol = left, right
                left -= 1
                right += 1
            
            #even
            left = i
            right = i+1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > maxLen):
                    maxLen = right - left + 1
                    leftSol, rightSol = left, right
                left -= 1
                right += 1

        return s[leftSol : rightSol + 1]

        