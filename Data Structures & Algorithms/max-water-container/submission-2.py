class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # my idea is to do two pointers, with one pointer at one and the other at the other end
        # don't i move the pointer wiht the bigger value?

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            dist = right - left
            min_val = min(heights[right], heights[left])
            area = min_val * dist
            if area > max_area:
                max_area = area

            if min_val == heights[left]:
                # move the smaller one, you want to look for nubmers to top the max
                left += 1
            else:
                right -= 1
        return max_area


        