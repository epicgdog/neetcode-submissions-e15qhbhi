class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force: O(n^2)
        # loop through each num and just calculate what the product is


        # linera time: 2 passes
        # first pass is to get all of teh left neighbors
        # second pass is to get all of the right neighbors
        r = [1] * len(nums)


        # left neighbors
        for i in range(1, len(nums)):
            r[i] *= nums[i-1] * r[i-1]

        # right neighbors
        for j in range(len(nums) - 2, -1, -1):
            r[j] *= nums[j+1]
            nums[j] *= nums[j+1]

        return r

            
            

        