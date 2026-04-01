class Solution:
    def isValid(self, s: str) -> bool:
        # must be greater htan 1
        n = len(s)
        if n < 2: return False

        # create a stack, holding the open parentheses
        # once you reach one of em closers, then we start popping from the stack
        # if the popped parentehses is the complimentary ot the current one, then we keep going
        # otherwise, we know its not the right order. 
        # ({[]})

        stack = []

        for i in range(n):
            current = s[i]
            if current == '(' or current == '{' or current == '[':
                stack.append(current)
                continue
            else:
                if len(stack) == 0: return False
                opener = stack.pop()
                if (opener == '(' and current != ')') or (opener == '[' and current != ']') or (opener == '{' and current != '}'):
                    return False

        return len(stack) == 0
