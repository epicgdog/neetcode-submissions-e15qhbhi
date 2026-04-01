class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea is to get the increasing portion basically if any
        # using sliding window

        n = len(prices)
        if n < 2: return 0

        i = 0
        j = 1
        max_profit = 0
        while j < n:
            profit  = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
            if profit < 0:
                i = j
            j = j + 1
                
        return max_profit



