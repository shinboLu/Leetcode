from collections import defaultdict
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = res = 0
        product = 1
        for right, value in enumerate(nums):
            product *= value
            while product >= k: 
                product /= nums[left]
                left += 1
            res += right-left+1
        return res 