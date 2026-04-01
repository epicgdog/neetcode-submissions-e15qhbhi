class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        i = 0

        while i < n:
            h = set()
            h.add(s[i])
            curr = 1
            j = i + 1
            while j < n and s[j] not in h:
                h.add(s[j])
                j = j + 1
                curr = curr + 1

            longest = max(curr, longest)
            i = i + 1

        return longest

            


        