#abcde

#cae

#brute force:
#recursion with param i, j
#base case i >= len(text1), j >= len(text2)
#if text1[i] == [j] then ans += 1
#and increment i++, j++ 
#recursively call f(i + 1) and f(j + 1)

#topdown
#same thing but @cache

#bottom up
#2d dp: dp[i][j] represents longest common subseq for text1[:i+1] and text2[:j+1]
#i, j goes backwards?

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] += 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
        '''
        def longestSubseqForIJ(i, j, ans):
            if i >= len(text1) or j >= len(text2):
                return ans
            if text1[i] == text2[j]:
                ans += 1
                return longestSubseqForIJ(i + 1, j + 1, ans)
            return max(longestSubseqForIJ(i + 1, j, ans), longestSubseqForIJ(i, j + 1, ans))
        return longestSubseqForIJ(0, 0, 0)
        '''
        
            