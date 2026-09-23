class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [math.inf] * len(cost)
        dp[0], dp[1] = 0, 0
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])