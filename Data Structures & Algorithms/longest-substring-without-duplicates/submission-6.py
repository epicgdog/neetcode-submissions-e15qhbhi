class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window that keeps expanding right if all different
        # move left pointer if similar one

        char_pos = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            if char in char_pos and char_pos[char] >= left:
                left = char_pos[char] + 1
            char_pos[char] = right
            if right - left + 1 > max_len:
                max_len = right - left + 1


        return max_len

                
