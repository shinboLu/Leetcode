class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:

        def kth_root_floor(n):
            if n < 0:
                return -1
            left = 0
            right = n
            while left < right:
                mid = (left+right+1)//2
                if mid ** k <= n: 
                    left = mid
                else:
                    right = mid -1
            return left
        
        return kth_root_floor(r) - kth_root_floor(l-1)
        
