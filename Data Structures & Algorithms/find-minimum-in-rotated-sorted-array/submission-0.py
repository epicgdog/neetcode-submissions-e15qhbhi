class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if know how many times rotated, 
        # easily figure out where the first number lies (0 + rotations)
        # max value of rotations is n
        # check the end and the start, if end > start, then do something?
        # move the right pointer until you get a number larger
        # then you check the diff

        l = 0
        r = len(nums)-1
        # 5 6 1 2 3 4
        # 3 4 5 6 1 2
        # 
        if nums[r] > nums[l]: return nums[l]

        # is this getting largest diff basically?
        while l < r:
            m = l + (r-l) // 2
            curr = nums[m]
            if curr > nums[r]:
                l = m + 1
            elif curr < nums[r]:
                r = m


        return nums[l]
                
        