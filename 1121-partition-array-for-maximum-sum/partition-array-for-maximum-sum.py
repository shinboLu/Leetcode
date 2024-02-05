class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}

        def dp(idx):
            if idx == len(arr):
                return 0
            if idx in memo:
                return memo[idx]
            cur_max = 0
            res = 0 

            for j in range(idx, min(len(arr), idx+k)):
                cur_max = max(cur_max, arr[j])
                window_size = j - idx + 1
                res = max(res, dp(j+1) + cur_max * window_size)
            memo[idx] = res
        
            return res 
        return dp(0)

        

