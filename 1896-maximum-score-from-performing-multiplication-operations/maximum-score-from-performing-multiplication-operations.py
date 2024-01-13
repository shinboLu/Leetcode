class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        dp = [[0] * (m+1) for _ in range(m+1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                    multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])


        print(dp)
        # dp[0] = nums 
        
        # for i in range(nrow):
        #     for j in range(ncol):
        #         dp[i][j] = multipliers[i] * nums[j] 

        # print(dp)
                

        return dp[0][0]