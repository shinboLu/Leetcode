class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}

        ## dfs will track at index i, the max sum of this index
        def dp(i):
            if i == len(arr):
                return 0

            if i in memo:
                return memo[i]
            
            cur_max = 0
            res = 0
            for j in range(i, min(len(arr), i+k)):
                cur_max = max(arr[j], cur_max)
                window_size = j - i + 1
                res = max(res, dp(j+1) + cur_max * window_size)
            memo[i] = res
            return res
        
        return dp(0)

                    