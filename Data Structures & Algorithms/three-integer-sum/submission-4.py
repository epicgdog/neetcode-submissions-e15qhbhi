class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # same idea as two sum
        # except each num in nums is a target (and negate)
        # nums[i] + nums[j] = -nums[k] <- target

        r = []
        found = set()
        hashmap = dict()
        # hash the entire thing first?
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for k in range(len(nums)):
            target = -nums[k]
            for i in range(len(nums)):
                if i == k: 
                    continue # no duplicates

                j_val = target - nums[i]
                if j_val not in hashmap: 
                    continue

                j = hashmap[j_val]
                
                if j == i or j == k:
                    continue

                arr = [nums[k], nums[i], nums[j]]
                key = tuple(sorted(arr))
                
                if key in found:
                    continue
                
                r.append(arr)
                found.add(key)
        return r
