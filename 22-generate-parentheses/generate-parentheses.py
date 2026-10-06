class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        tempstr = []
        def backtrack(opencount, closedcount):
            if opencount == closedcount == n:
                ans.append("".join(tempstr))
            if opencount <= n:
                tempstr.append("(")
                backtrack(opencount + 1, closedcount)
                tempstr.pop()
            if opencount > closedcount:
                tempstr.append(")")
                backtrack(opencount, closedcount + 1)
                tempstr.pop()
        backtrack(0, 0)
        return ans