class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_sum = sum(nums)
        # 和为奇数时，不可能划分成两个和相等的集合
        if tot_sum % 2 != 0:
            return False
        n = len(nums)
        tot_sum = tot_sum // 2
        # 定义二维数组 dp
        dp = [[False] * (tot_sum + 1) for _ in range(n + 1)]
        # base case
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, tot_sum + 1):
                if j - nums[i - 1] < 0:
                    # 背包容量不足，不能装入第 i 个物品
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装入或不装入背包
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[n][tot_sum]