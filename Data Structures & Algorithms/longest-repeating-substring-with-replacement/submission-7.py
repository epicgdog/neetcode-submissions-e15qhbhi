from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force: go through each possible substring, choose k characters and see if it is the largest substring
        # however, we don't really need to do this when we don't 
        # have to return a substring, we just neeed its length
        # we could define a boundary to check like left and right
        # to act as our substring
        

        # we don't really need to loop through every possible substring
        # either. we only care about the frequencies, and the frequency
        # of each character is constant. we just need to add/subtract
        # once we move the boundaries around

        # the idea is to loop through all the characters (right index)
        # calculate the most frequent character's value
        # window size - max = chars to replace
        # if chars to replace is more htan k, not a valid substring to be considered
        # to fix, we move the left pointer up until it is valid
        # find the max and return

        freq_map = defaultdict(int)
        left = 0
        len_s = len(s)
        max_len = 0

        for right in range(len_s):
            freq_map[s[right]] += 1
            max_count = max(freq_map.values())
            while right - left + 1 - max_count > k:
                # move left to force valid
                freq_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)


        return max_len

            

            


    



         