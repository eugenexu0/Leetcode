class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s: str, ans: str, ansArray: List[str], wordDict: List[str]):
            if (len(s) == 0):
                ansArray.append(ans[:-1])
            for i in range(len(s)):
                if (s[0:i+1] in wordDict):
                    #include
                    helper(s[i+1:], ans + s[0:i+1] + " ", ansArray, wordDict)
        ansArray = []
        ans = ""
        helper(s, ans, ansArray, wordDict)
        return ansArray