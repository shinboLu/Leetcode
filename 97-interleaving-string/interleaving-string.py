class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        nrow = len(s1)
        ncol = len(s2)

        if nrow + ncol != len(s3):
            return False

        dp = [[False] * (ncol+1) for _ in range(nrow+1)]
        dp[0][0] = True
        
        for i in range(1, nrow+1):

            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1, ncol+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1] 

        for i in range(1, nrow+1):
            for j in range(1, ncol + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        print(dp)

        return dp[nrow][ncol]

