class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []
        minremovals = math.inf
        def backtrack(i, tempstr: list[str], opencount, removalcount):
            nonlocal minremovals, ans
            #print(f'{i=}. {tempstr=}, {opencount=}, {removalcount=}')
            if removalcount > minremovals:
                return
            if i == len(s):
                if opencount == 0 and removalcount <= minremovals:
                    #reset if we found better
                    if removalcount < minremovals:
                        minremovals = removalcount
                        ans = []
                    ans.append((removalcount, tempstr[:]))
                return
            
            #skip
            if s[i] == "(" or s[i] == ")":
                backtrack(i + 1, tempstr, opencount, removalcount + 1)
            #take
            if s[i] == "(":
                opencount += 1
            elif s[i] == ")":
                opencount -= 1
            if opencount >= 0:
                tempstr.append(s[i])
                backtrack(i + 1, tempstr, opencount, removalcount)
                tempstr.pop()
        
        backtrack(0, [], 0, 0)
        ans.sort()
        #print(ans)
        newans = set()
        for removals, string in ans:
            if removals == minremovals:
                newans.add("".join(string))
            else:
                break
        return list(newans)