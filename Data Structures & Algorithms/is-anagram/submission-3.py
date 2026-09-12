from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_map = defaultdict(int)
        for ch in s:
            s_freq_map[ch] += 1

        t_freq_map = defaultdict(int)
        status = 0
        for ch in t:
            if ch not in s_freq_map or t_freq_map[ch] >= s_freq_map[ch] :
                return False

            t_freq_map[ch] += 1
            status += 1

        return status == len(s)
            


        