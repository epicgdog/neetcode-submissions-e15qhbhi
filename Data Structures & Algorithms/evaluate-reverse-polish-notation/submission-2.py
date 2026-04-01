class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep putting numbers into stack until reach an operator
        # do operation of the numbers  and then put result back int eh stack
        # repeat 

        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                second = stack.pop()
                first = stack.pop()
                ans = 0
                if token == '/':
                    ans = int(first/second)
                elif token == '+':
                    ans = first+second
                elif token == '-':
                    ans = first-second
                elif token == '*':
                    ans = first*second

                stack.append(ans)
            else:
                stack.append(int(token))

        return stack[0]