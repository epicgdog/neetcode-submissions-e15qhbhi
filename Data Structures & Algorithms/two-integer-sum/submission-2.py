class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimal
        # build a dictionary, storing every item and index
        # loop through each item and look for target - the current one
        # to see if there exists the number to  current +  n to target
        # this would be saved


        d = {}
        for i in range(len(nums)):
            # when we find something that finds that number
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            # usual
            d[nums[i]] = i


        return []
