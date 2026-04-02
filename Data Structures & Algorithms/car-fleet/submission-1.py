class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # solution!
        # was overthinking the simulation.
        # first, you want to sort by position (i thought of this but lowkey was i thought would affect performance too much)
        # then, you basically calculate teh amount of time it takes to get to destination and put on the stack
        # if the time is less than or equal, you kown they will reach the destination at the same time, so you remove the fleetcount
        # if its greater, thats like the time to beat
        # instead of doin g all of the monotonic stack stuff, sorting allows you to assume that the top of the stack is the next previous that you can look to
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
                
