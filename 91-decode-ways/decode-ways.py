class Solution:
    def numDecodings(self, s: str) -> int:
        #11 -> 1, 1 and 11 (2)
        #111 -> 11, 1 and 1, 11 and 1,1,1 (3)
        #1111 -> 11, 1, 1 and 1, 1, 11 and 1, 11, 1, and 11, 11, and 1, 1, 1, 1 (5)
        #11111 -> (8)
        #fibonnaci seq
        #BUT if we add a 0:
        #111110 -> (5)
        #12 -> 1, 2 and 12
        #123 -> 1, 2, 3, and 12, 3, and 1, 23
        #1234 -> 1, 2, 3, 4 and 12, 3, 4 and 1, 23, 4
        if int(s[0]) == 0:
            return 0
        if len(s) == 1:
            return 1
        if int(s[1]) == 0:
            if int(s[0]) != 1 and int(s[0]) != 2:
                return 0
        prev2 = 1
        prev1 = 2 if int(s[:2]) <= 26 and int(s[1]) != 0 else 1
        for i in range(2, len(s)):
            curr = 0
            check = s[i - 1:i + 1]
            if int(check[1]) == 0:
                if int(check[0]) != 1 and int(check[0]) != 2:
                    return 0
                curr = prev2
            elif 10 <= int(check) <= 26:
                curr = prev2 + prev1
            else:
                curr = prev1
            prev2, prev1 = prev1, curr
        return prev1