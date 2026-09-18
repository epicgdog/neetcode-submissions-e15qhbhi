class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the idea is similar to the pivot, but instead of finding the pivot, you would be finding the target instead
        # insteda you would compar ethe target to the mid


        len_nums = len(nums)
        left = 0 
        right = len_nums - 1

        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target: 
                return right

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


        