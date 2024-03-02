class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = float('-inf')

        while left < right:
            cur_length = right - left 
            cur_height = min(height[left], height[right])
            cur_fill = cur_length * cur_height
            res = max(res, cur_fill) 

            if height[left] <= height[right]:
                left += 1
            else:
                right-=1
        return res 
