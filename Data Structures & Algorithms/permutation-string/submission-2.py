from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 > s2, won't exist.
        # sliding window with length of s1
        # compare contents of window if character is not in there, keep moving on
        # if all are there return true

        if len(s1) > len(s2): return False

        h1 = defaultdict(int)
        h2 = defaultdict(int)
        # this only gets the frequencies for as large as s1
        for i in range(len(s1)):
            h1[s1[i]] += 1
            h2[s2[i]] += 1

        matches = 0
        # so we need to check it basically
        matcher = "abcdefghijklmnopqrstuvwxyz"
        for key in matcher:
            if h1[key] == h2[key]:
                matches += 1

        # now is teh actual sliding window portion
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            right_char = s2[r]
            left_char = s2[l]

            h2[right_char] += 1
            if h2[right_char] == h1[right_char]:
                matches += 1
            elif h2[right_char] - 1 == h1[right_char]:
                matches -= 1

            h2[left_char] -= 1
            if h2[left_char] == h1[left_char]:
                matches += 1
            elif h2[left_char] + 1 == h1[left_char]:
                matches -= 1

            l += 1
        
        return matches == 26

    


