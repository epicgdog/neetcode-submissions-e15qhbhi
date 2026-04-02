class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find the next least thing for each position and keep track
        # keep a set of the cars you will be tracking, can probably just keep track of the smallest one and break once that one is done. 
        # find the largest car position and set as the starting point for updates
        # increment the hours until no cars are left to track
        # increment the position of the largest position first, based on speed and stuff. 
        # then using the stack trickle it down to its neighbors
        # so then when the neighbor reaces and caluclates speed, basically comparing to the calculated parent
        # if larger, then just match the speed and go to the next until you hit -1. 
        merged = list(zip(position, speed))
        merged.sort(reverse=True)
        stack = []
        n = len(position)
        fleet_count = n
        for i in range(n):
            car = merged[i]
            time_to_dest = (target - car[0])/car[1]
            if len(stack) > 0 and time_to_dest <= stack[-1]:
                fleet_count -= 1
            else: 
                stack.append(time_to_dest)

        return fleet_count
                
