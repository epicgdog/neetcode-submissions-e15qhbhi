class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep putting numbers into stack until reach an operator
        # do operation of the numbers  and then put result back int eh stack
        # repeat 

        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                second = int(stack.pop())
                first = int(stack.pop())
                ans = 0
                if token == '/':
                    ans = int(first/second)
                else:
                    ans = eval(f"{first}{token}{second}")

                stack.append(ans)
            else:
                stack.append(token)

        return int(stack[0])