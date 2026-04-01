class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of the nums
        # is num + 1 in there
        s = set(nums)
        longest = 0
        for num in s:
            curr_total = 1
            curr_num = num
            while curr_num + 1 in s:
                curr_total += 1
                curr_num += 1
            longest = max(curr_total, longest)

        return longest
        