from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = dict()

        for x in nums:
            if x in freq_map:
                return True
            freq_map[x] = 1
        
        return False

        