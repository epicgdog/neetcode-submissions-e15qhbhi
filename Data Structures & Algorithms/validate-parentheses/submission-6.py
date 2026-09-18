class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                if len(st) > 0:

                    open_bracket = st.pop()
                    if open_bracket == '(' and ch != ')' or open_bracket == '{' and ch != '}' or open_bracket == "[" and ch != ']':
                        return False
                else:
                    return False

        return len(st) == 0

        