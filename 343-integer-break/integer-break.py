class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [0] * (n+1)
        for i in [1,2,3]:
            dp[i] = i

        for num in range(4, n+1):
            res = num
            for i in range(2, num):
                res = max(res, i * dp[num-i])
    
            dp[num] = res

        return dp[-1]

        