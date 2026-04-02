import math

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max value of k has to be the max value of piles
        # find the minimum; binary search between 1 and max value of k
        # each pile will take at least 1 hour to finish; decimal will take more
        k = max(piles)
        l = 1
        r = k
        while l <= r:
            m = l + (r-l) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/m)

            if total_hours <= h:
                k = m
                r = m-1
            else:
                l = m+1
                
        return k

        


        