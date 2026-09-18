from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two frequency maps
        # window of a substring, move hte lfet pointer while the
        # frequency maps are the same
        # we can also just count the number of characters we are off by
        # that way we won't have ot compare the entire frequency map
        
        len_s = len(s)
        len_t = len(t)

        if len_t > len_s:
            return ""

        # we need the freq map of t in order to verify 
        # the counts from s
        t_freq_map = defaultdict(int)
        for ch in t:
            t_freq_map[ch] += 1


        left = 0
        done = 0
        min_sub_len = 0
        min_left = 0
        min_right = -1
        s_freq_map = defaultdict(int)

        for right in range(len_s):
            s_freq_map[s[right]] += 1
            if t_freq_map[s[right]] >= s_freq_map[s[right]]:
                # progress
                done += 1
                if done == len_t:

                    # truncate until you can't
                    while s[left] not in t or s_freq_map[s[left]] > t_freq_map[s[left]]:
                        s_freq_map[s[left]] -= 1
                        left += 1
                    
                    # calculate the substring length n compare
                    sub_len = right - left + 1
                    if min_sub_len == 0 or sub_len < min_sub_len:
                        min_sub_len = sub_len
                        min_left = left
                        min_right = right
                    
                    s_freq_map[s[left]] -= 1
                    done -= 1
                    left += 1


        return s[min_left:min_right+1]
            



        
        

      