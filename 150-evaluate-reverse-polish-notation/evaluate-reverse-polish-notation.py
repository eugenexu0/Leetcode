class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            #print(stack)
            if s.isnumeric() or (s.startswith('-') and s[1:].isnumeric()):
                stack.append(int(s))
            else:
                a, b = stack.pop(), stack.pop()
                #print(f'a {a} b {b}')
                if s == "+":
                    stack.append(b + a)
                elif s == "-":
                    stack.append(b - a)
                elif s == "*":
                    stack.append(b * a)
                elif s == "/":
                    stack.append(int(b / a))
        return stack[0]