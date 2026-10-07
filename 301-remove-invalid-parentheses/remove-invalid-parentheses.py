class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []
        minremovals = math.inf
        def backtrack(i, tempi, tempstr, opencount, removalcount):
            nonlocal minremovals, ans
            if removalcount > minremovals:
                return
            if i == len(s):
                if opencount == 0 and removalcount <= minremovals:
                    #reset if we found better
                    if removalcount < minremovals:
                        minremovals = removalcount
                        ans = []
                    ans.append((removalcount, tempstr))
                return
            
            #print(f'{i=}. {tempi=} , {tempstr=}, {opencount=}')
            #skip
            if s[i] == "(" or s[i] == ")":
                if tempi + 1 == len(s):
                    backtrack(i + 1, tempi, tempstr[:tempi], opencount, removalcount + 1)
                elif tempi == 0:
                    backtrack(i + 1, tempi, tempstr[tempi + 1:], opencount, removalcount + 1)
                else:
                    backtrack(i + 1, tempi, tempstr[:tempi] + tempstr[tempi + 1:], opencount, removalcount + 1)
            #take
            if s[i] == "(":
                opencount += 1
            elif s[i] == ")":
                opencount -= 1
            if opencount >= 0:
                backtrack(i + 1, tempi + 1, tempstr, opencount, removalcount)
        
        backtrack(0, 0, list(s), 0, 0)
        ans.sort()
        #print(ans)
        newans = set()
        for removals, string in ans:
            if removals == minremovals:
                newans.add("".join(string))
            else:
                break
        return list(newans)