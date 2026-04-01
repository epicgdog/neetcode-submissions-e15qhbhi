class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # optimal
        # sort the array first
        # go through each one
        # use two pointers to determine if current sum is to large or not, otherwise decrement

        nums.sort()
        r = []
        l = len(nums)

        for target_index in range(l):
            if nums[target_index] > 0:
                break
            elif target_index != 0 and nums[target_index] == nums[target_index-1]:
                continue

            low = target_index+1
            high = l-1

            target = -nums[target_index]
            while low < high:
                sum = nums[low] + nums[high]
                if sum > target:
                    high = high - 1
                elif sum < target:
                    low = low + 1
                else:
                    r.append([nums[target_index], nums[high], nums[low]])
                    # now we make sure there are no duplicates
                    low = low  + 1
                    high = high - 1

                    while low < high and nums[low] == nums[low-1]:
                        low = low + 1
                    while low < high and nums[high] == nums[high+1]:
                        high = high - 1
        return r;
                        

                    
        
        