from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 > s2, won't exist.
        # sliding window with length of s1
        # compare contents of window if character is not in there, keep moving on
        # if all are there return true

        if len(s1) > len(s2): return False

        k = len(s1)
        h = defaultdict(int)
        for ch in s1:
            h[ch] += 1
        
        l = 0
        n = len(s2)
        for r in range(k-1, n):
            # freq of current window
            h2 = defaultdict(int)
            for i in range(l, r+1):
                h2[s2[i]] += 1
            if h2 == h: return True
            l += 1
        return False


