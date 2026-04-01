class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack: basically trying to find next greatest or next least
        # initialize a stack
        # for each temperature, compare to the top of teh stack
        # if current > top of stack, we know this is out of order, so we know the current number is greater than the top one
        # calc the distance and set it
        # keep popping until its empty or the top is greater than or equal to teh current. 

        stack = []
        n = len(temperatures)
        r = [0] * n
        
        for i in range(n):
            temp = temperatures[i]
            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                index = stack.pop()
                r[index] = i - index

            stack.append(i) 

        return r