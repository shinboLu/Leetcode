class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        res = float('-inf')

        while left < right:
            cur_h = min(height[left], height[right])
            cur_l = right-left
            cur_area = cur_h * cur_l
            res = max(res, cur_area)

            if height[left] > height[right]:
                right-=1
            else:
                left+=1

        return res
