class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        res = float('-inf')

        while left < right:
            h1 = min(height[left], height[right])
            w1 = right-left
            cur_area = h1*w1
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
            res = max(cur_area, res)

        return res