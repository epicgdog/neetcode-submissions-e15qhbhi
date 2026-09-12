class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            # is there a number in the hashmap that equals target - nums[i]
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i
        return []

        