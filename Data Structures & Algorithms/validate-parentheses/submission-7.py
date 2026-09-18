class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            elif len(st) == 0:
                return False
            else:
                open_bracket = st.pop()
                if open_bracket == '(' and ch != ')' or open_bracket == '{' and ch != '}' or open_bracket == "[" and ch != ']':
                    return False

        return len(st) == 0

        