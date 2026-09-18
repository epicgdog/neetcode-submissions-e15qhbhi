class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum element in O(n): basically you loop through and check the item in front or behidn if it is increasing

        # log(n) -> binary search for sure
        # we can tell if something is pivoted if both ends are still icnreasing
        # if left > right -> know its been rotated
        # get mid point, and shift left to mid if still greater than


        len_nums = len(nums)
        left = 0
        right = len_nums - 1 

        if nums[right] > nums[left]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

        