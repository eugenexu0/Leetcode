class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ans = []
        for n in asteroids:
            if n > 0:
                stack.append(n)
            else:
                exploded = False
                while stack and not exploded:
                    top = stack[-1]
                    tempn = -n
                    if tempn == top:
                        stack.pop()
                        exploded = True
                    elif tempn > top:
                        stack.pop()
                    else:
                        exploded = True
                if not exploded:
                    ans.append(n)
            #print(f'{stack=}')
        ans.extend(stack)
        return ans
                