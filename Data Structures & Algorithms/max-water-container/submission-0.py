class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # go thorugh each and everyone and compare and make sure that it is the most amount
        n = len(heights)
        # curr_max = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         if area > curr_max:
        #             curr_max = area

        # return curr_max

        # better
        # two pointer, move the min height
        i = 0
        j = n-1
        max_area = 0

        while i < j:
            curr_min = min(heights[i], heights[j])
            area = curr_min * (j - i)
            if area > max_area:
                max_area = area
            if curr_min == heights[i]:
                i += 1
            else:
                j -= 1

        return max_area

        