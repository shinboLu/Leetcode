class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        res = float('-inf')

        while left < right:
            cur_wid = right-left
            cur_hei = min(height[left], height[right])
            area = cur_wid * cur_hei
            res = max(res, area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            
        return res
                