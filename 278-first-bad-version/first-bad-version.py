# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n 

        while left <= right:
            mid = (left+right)//2
            print(mid)
            if isBadVersion(mid)==False:
                left = mid+1
            else:
                right = mid -1 
        return left