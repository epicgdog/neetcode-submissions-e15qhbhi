class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome, should be the same reading forwards and backwards
        # case insensitive and ignores anything that is non-alphanumeric
        # two pointers, one to left and one to right
        # while left < right do stuff
        s = s.lower()
        left = 0
        right = len(s) -1 
        while left < right:

            # need to take into account non-alphanumeric, and then also case insensitive
            if not s[left].isalnum():
                left += 1
                continue
        
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
        