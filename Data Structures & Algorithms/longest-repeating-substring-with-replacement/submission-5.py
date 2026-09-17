from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start with the first character and loop through all the character
        # count the number of characters that are the same in a given substring of length k
        # len - same = num to replace
        # if num to replace > k, move left to be valid
        # else continue and save hte max length

        freq_map = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            freq_map[s[right]] += 1
            max_count = max(freq_map.values())

            while left < right and (right - left + 1) - max_count > k:
                freq_map[s[left]] -= 1
                left += 1

            window_size = right - left + 1
            if window_size > max_len:
                max_len = window_size

            
        return max_len

    



         