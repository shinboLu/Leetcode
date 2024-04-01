class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = (ay2 - ay1) * (ax2 - ax1)
        a2 = (by2 - by1) * (bx2 - bx1) 

        tot_area = a1 + a2


        left_x = max(ax1, bx1)
        right_x = min(ax2, bx2) 
        overlap_l = right_x - left_x

        top_x = min(ay2, by2) 
        bot_x = max(ay1, by1) 
        overlap_h = top_x - bot_x

        overlap_a = 0 

        if overlap_l > 0 and overlap_h > 0:
            overlap_a = overlap_h * overlap_l 

        return tot_area - overlap_a
