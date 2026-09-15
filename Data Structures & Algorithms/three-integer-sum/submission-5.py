class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # same idea as two sum
        # except each num in nums is a target (and negate)
        # nums[i] + nums[j] = -nums[k] <- target

        r = []
        nums = sorted(nums)

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            target = -nums[k]

            # don't care about anything below it, not gonna help
            # negative number not gonna help get to a positive u feel me
            left = k+1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    r.append([nums[k], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif curr_sum > target:
                    #overshot, move the right back
                    right -= 1
                else:
                    left += 1
        return r
