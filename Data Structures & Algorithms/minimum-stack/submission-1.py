class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.global_min = None
        

    def push(self, val: int) -> None:
        if self.global_min == None or val <= self.global_min:
            self.min_stack.append(self.global_min)
            self.global_min = val

        self.stack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.global_min:
            self.global_min = self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.global_min
        
