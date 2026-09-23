class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(amount + 1):
            if i == math.inf:
                continue
            for c in coins:
                if i + c > amount:
                    continue
                dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1] if dp[-1] != math.inf else -1
