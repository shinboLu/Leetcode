class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        def check(window_size):
            for r in range(window_size-1, n):
                l = r - window_size + 1 
                tot = prefix[r+1] - prefix[l]
                target = nums[r]
                cost = target * window_size - tot
                if cost <= k:
                    return True
            return False

        left = 1
        right = n 
        res = 1
        while left <= right:
            mid = (left+right)//2 
            if check(mid):
                res = mid
                left = mid+1 
            else:
                right = mid-1
        return res