class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                if c == ')' and l[-1] != '(':
                    return False
                if c == ']' and l[-1] != '[':
                    return False
                if c == '}' and l[-1] != '{':
                    return False
                l.pop()
        return len(l) == 0