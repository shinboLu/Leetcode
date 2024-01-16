class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n+1):
            cur = nums[i-1]

            for j in range(target + 1):
                if j < cur:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-cur] 


        #print(dp)
        
        return dp[n][target]
                