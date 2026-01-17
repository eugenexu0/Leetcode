class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestSeen, maxProfit = prices[0], 0
        for index, val in enumerate(prices):
            #change lowest
            if val < lowestSeen:
                lowestSeen = val
            #calculate potential profit
            else:
                potential = val - lowestSeen
                if potential > maxProfit:
                    maxProfit = potential
        return maxProfit

            