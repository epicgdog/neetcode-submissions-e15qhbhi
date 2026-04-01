class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force: 
        # inner 3 loops and then do stuff
        r = []
        r_set = set()



        # can't you just do two sum len(nums) times?
        for i in range(len(nums)):
            # each target is nums[i]
            # then don't search for each thing
            target = -nums[i]
            d = {}
            for j in range(len(nums)):
                diff = target-nums[j]
                if diff in d and j != d[diff] and i != d[diff] and i != j:
                    set_check = tuple(sorted((nums[i], nums[j], diff)))
                    if not set_check in r_set:
                        r_set.add(set_check)
                        r.append([nums[i], nums[j], diff])

                d[nums[j]] = j
                   




        return r;
                        

                    
        
        