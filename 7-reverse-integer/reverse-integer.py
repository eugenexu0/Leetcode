class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        INT_MAX = 2**31 - 1

        is_neg = False
        if x < 0:
            is_neg = True
            x = -x

        for i in range(len(str(x))):
            temp = x % 10

            #check if overflow
            #LOGIC: if ans * 10 + temp > MAX
            #but to avoid overflow:
            if ans > (INT_MAX - temp) // 10:
                return 0

            ans = ans * 10 + temp
            x = x // 10
        
        if is_neg:
            return -ans
        return ans

