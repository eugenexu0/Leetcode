#brute force -- for first letter in s, check every word in wordDict
#if word matches, shrink s and repeat
#note multiple words can match

#trie -- similar idea, makes it easier to check every word in worddict (prefix)

#possible dp sol?

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        ans = False
        @cache
        def searchWordAndShrink(tempstr):
            nonlocal ans
            if tempstr == "":
                ans = True
            for i in range(longest):
                if tempstr[:i + 1] in wordSet:
                    searchWordAndShrink(tempstr[i + 1:])
        longest = len(max(wordDict, key=len))
        wordSet = set(wordDict)
        searchWordAndShrink(s)
        return ans