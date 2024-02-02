class Solution:
    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n-1
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n+1):
            res = i  
            for j in range(2, i): 
                res = max(res, j * dp[i-j])
            dp[i] = res
        return dp[-1]