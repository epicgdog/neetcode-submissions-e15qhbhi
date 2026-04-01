class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3: return 0

        i = 0
        j = n-1
        max_left = 0
        max_right = 0
        rainwater = 0

        while i < j:
            if height[i] <= height[j]:
                rainwater = rainwater + max(max_left - height[i], 0)
                max_left = max(max_left, height[i])
                i = i + 1
            else:
                rainwater = rainwater + max(max_right - height[j], 0)
                max_right = max(max_right, height[j])
                j = j - 1
        return rainwater


            

        # a lot like maximum container, you have two pointers and try to find the maximum amount of rain water
        # always move the minimum; this is where the limit is always, or the maximum amaount of rainwater that can be held
        # 

        