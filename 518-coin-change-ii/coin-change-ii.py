class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        arr = [0] * (amount + 1)
        arr[0] = 1
        for coin in coins:
            for index in range(1, amount+1):
                if index >= coin:
                    arr[index] += arr[index - coin]
                

        return arr[amount]



        