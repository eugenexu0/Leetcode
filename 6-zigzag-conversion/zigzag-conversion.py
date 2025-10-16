class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #1 -> 0
        #2 -> 2
        #3 -> 4
        #4 -> 6
        #5 -> 8
        #6 -> 10
        if numRows == 1:
            return s
        currRow = 0
        ans = ""
        while currRow < numRows:
            i = currRow
            while i < len(s):
                ans += s[i]
                i += (numRows - 1) * 2
                jumpBack = i - currRow * 2
                if (currRow != 0 and currRow != (numRows - 1) and jumpBack < len(s)):
                    ans += s[jumpBack]
                print(ans)
            currRow += 1
        return ans