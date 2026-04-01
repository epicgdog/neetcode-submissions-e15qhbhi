class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this one you can basically a forward and backward pass
        # in the forward pass, we simply accumulate all of the products to the left of the index
        # for the backward pass, we keep a variable with the currnet product and multiply it to the accumulation of products
        # then you are good

        n = len(nums)
        if n < 2: return nums
        
        arr = [1] * n
        for i in range(1, n):
            arr[i] = nums[i-1] * arr[i-1]

        right_product = 1
        for j in range(n-2, -1, -1):
            right_product *= nums[j + 1]
            arr[j] *= right_product

        return arr

