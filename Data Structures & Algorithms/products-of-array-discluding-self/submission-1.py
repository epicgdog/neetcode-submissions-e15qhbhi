class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force: O(n^2)
        # loop through each num and just calculate what the product is


        # linera time: 2 passes
        # first pass is to get all of teh left neighbors
        # second pass is to get all of the right neighbors
        hashmap_left = dict()
        hashmap_right = dict()
        for idx in range(len(nums)):
            hashmap_left[idx] = 1 # initialize to 1 for multiplication
            hashmap_right[idx] = 1


        # left neighbors
        for i in range(1, len(nums)):
            hashmap_left[i] *= nums[i-1] * hashmap_left[i-1]

        # right neighbors
        for j in range(len(nums) - 2, -1, -1):
            hashmap_right[j] *= nums[j+1] * hashmap_right[j+1]

        for key in hashmap_left:
            nums[key] = hashmap_left[key] * hashmap_right[key]

        return nums

            
            

        