class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the idea here is to make a sliding window. 
        # i just picture a trading vue thingy
        # ride all the hills, and once negative, move the window over


        starting = 0
        curr_profit = 0
        max_profit = 0
        for i in range(len(prices)):
            # only add to the current if it is increasing
            # else we will move the starting to that point and continue counting 
            # as long as it is increasing
            # we only care about increasing and never decreasting if we wnat to maximize profit
            diff = prices[i] - prices[starting]

            if diff < 0:
                # decreasing, move startinga nd reset the profit counter
                starting = i
                if curr_profit > max_profit:
                    max_profit = curr_profit
                curr_profit = 0
            else:
                curr_profit = diff
                if curr_profit > max_profit:
                    max_profit = curr_profit

            
        return max_profit