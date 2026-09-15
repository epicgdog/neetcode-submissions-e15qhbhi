class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # same idea as two sum
        # except each num in nums is a target (and negate)
        # nums[i] + nums[j] = -nums[k] <- target

        r = []
        found = set()

        for k in range(len(nums)):
            target = -nums[k]
            hashmap = dict()
            for i in range(len(nums)):
                if i == k: 
                    continue # no duplicates

                if target - nums[i] in hashmap:

                    arr = [nums[k], nums[i], nums[hashmap[target - nums[i]]]]

                    key = tuple(sorted(arr))
                    
                    if key in found:
                        continue
                    
                    r.append(arr)
                    found.add(key)
                else:
                    hashmap[nums[i]] = i
        return r
