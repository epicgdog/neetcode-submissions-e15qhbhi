class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums:
            if i in d.values(): return True

            d[i] = i

        return False
        