from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force: sliding the window and then trying every single possible combination until we reach the end
        # another key thing is a substring u can't put the characters out of order, just truncated version fo the string
        # ok its not that bad i think
        # i came up with the idea that we make a sliding window that only expands as long as there are replacements and 
        # maintains a consecutive amount of characters
        # there will be a hashmap that counts the frequency of charactres in the current window.
        # the numbers don't change evne with replacements, that will be like an offset, like oh this and this led to yeah
        # reduce the amount when you shift the left pointer over as well

        h = defaultdict(int)
        l = 0
        n = len(s)
        maxf = 0
        res = 0

        for r in range(n):
            # go by character as the hashmap basically saves that stuff
            ch = s[r]
            h[ch] += 1
            maxf = max(maxf, h[ch])

            while maxf + k < r - l + 1:
                h[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)


        return res









