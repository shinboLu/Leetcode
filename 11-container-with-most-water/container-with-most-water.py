class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = float('-inf')

        while left < right:
            cur_len = right - left
            cur_hei = min(height[left], height[right])
            cur_area = cur_len * cur_hei
            res = max(cur_area, res)

            if height[left] <= height[right]:
                left +=1
            else:
                right-=1 

        return res 
