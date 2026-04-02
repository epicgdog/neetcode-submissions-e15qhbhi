class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if left > right, we know its rotated
        # fidn the inflection point by binary search: if mid > right: we know this is still part of the rotated part, if < right
        # find the target in between the inflectino point or just hte basic binary search basically
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

