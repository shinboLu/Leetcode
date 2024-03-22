class Solution:
    def countVowelStrings(self, n: int) -> int:
        vn = 5
        dp = [[0] * (vn+1) for _ in range(n+1)]

        for i in range(1, vn+1): 
            dp[1][i] = i

        for j in range(1, n+1):
            dp[j][1] = 1

        for i in range(2, n+1):
            for j in range(2, vn+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        return dp[-1][-1]



