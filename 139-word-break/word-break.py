#brute force -- for first letter in s, check every word in wordDict
#if word matches, shrink s and repeat
#note multiple words can match

#trie -- similar idea, makes it easier to check every word in worddict (prefix)

#possible dp sol?

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        #top down: recursive (substr -> bool)
        #optimize: index -> bool (instead of substr)
        #bottom up: dp[i] -> bool (can we reach s[:i]?)
        #recurrence relation: dp[i] = True if dp[i - len(word)] and s[i - len(word):i] == word
        #base case: dp[0] = True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if not dp[i]:
                    dp[i] = dp[i - len(word)] and s[i - len(word):i] == word
                #print(f'{word=}, {i=}, {s[:i]=}, {dp[i]=}')
        return dp[-1]
                