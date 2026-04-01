class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        chars = set()
        l = 0

        for r in range(n):
            while s[r] in chars:
                chars.remove(s[l]) # remove the leftmost
                l = l + 1
            chars.add(s[r])
            longest = max(longest, r - l + 1) # since 1 char length of 1

        return longest


        