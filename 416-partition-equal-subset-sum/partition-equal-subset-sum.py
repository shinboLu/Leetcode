class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False

        target = nums_sum // 2 
        n = len(nums)

        dp = [[False] * (target+1) for _ in range(n+1)]
        dp[0][0] = True

        ## i is the ith number in nums
        for i in range(1, n+1):
            cur_num = nums[i-1]

            # j is the jth sum in range(target)
            for j in range(target+1):
                if j < cur_num: 
                    print(dp[i][j-1], i, j-1)
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-cur_num]

        return dp[-1][-1]


                

                
                