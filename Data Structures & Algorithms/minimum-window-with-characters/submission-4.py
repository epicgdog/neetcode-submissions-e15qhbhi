from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # my original high level approach was correct
        # move right if no matches for characters in t
        # move left if matches for characters in t
        # i should've used hashmaps in the beginning to count
        # i forgot about the defaultdict method
        # so you basically start the left n right index at the same point
        # move the rihgt index as long as you have as status in not equal to the length, meaning it didn't check all the boxes
        # once it does, we use the left index, and shorten the substring until it doesn't fulfill t
        # then redo again

        t_len = len(t)
        s_len = len(s)

        if t_len > s_len:
            return ""

        # construct the t map as the reference
        t_map = defaultdict(int)
        for ch in t:
            t_map[ch] += 1

        left_idx = 0
        right_idx = 1 # exclusive
        best_left = 0
        best_right = 0
        min_len = 0

        # setup the map
        s_map = defaultdict(int)
        s_status = 0

        for right_idx in range(s_len):
            if s[right_idx] in t_map:
                right_most_ch = s[right_idx]
                s_map[right_most_ch] += 1
                if s_map[right_most_ch] <= t_map[right_most_ch]:
                    s_status += 1

            while s_status == t_len:
                # possible solution
                sub_len = (right_idx+1) - left_idx
                if min_len == 0 or sub_len < min_len:
                    best_left = left_idx
                    best_right = right_idx
                    min_len = sub_len
                left_most_char = s[left_idx]
                if left_most_char in t_map:
                    s_map[left_most_char] -= 1
                    if s_map[left_most_char] < t_map[left_most_char]:
                        s_status -= 1
                left_idx += 1

        return s[best_left:best_right+1] if min_len > 0 else ""
        

    
        
        