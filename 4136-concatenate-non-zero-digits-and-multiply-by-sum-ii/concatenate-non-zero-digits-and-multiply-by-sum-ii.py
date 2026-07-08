class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        ans = []
        prefix = [0]
        prefsum = [0]
        numNonZero = [0]
        pow10 = [1] * (len(s) + 1)

        for i in range(len(s)):
            pow10[i + 1] = (pow10[i] * 10) % MOD
    
        for i in range(len(s)):
            pre = int(s[i])
            if pre != 0:
                prefix.append((prefix[i] * 10 + pre) % MOD)
                prefsum.append(prefsum[i] + pre)
                numNonZero.append(numNonZero[i] + 1)
            else:
                prefix.append(prefix[i])
                prefsum.append(prefsum[i])
                numNonZero.append(numNonZero[i])
        # print(f'{prefix=}')
        # print(f'{prefsum=}')
        # print(f'{numNonZero=}')
        for start, end in queries:
            pre = prefix[start]
            post = prefix[end+1]
            countNonZero = numNonZero[end+1] - numNonZero[start]
            x = (post - pre * pow10[countNonZero]) % MOD
            sumDigits = prefsum[end+1] - prefsum[start]
            # print(f'{countNonZero=}')
            # print(f'{x=}')
            # print(f'{sumDigits=}')
            ans.append(x * sumDigits % MOD)
        return ans
    