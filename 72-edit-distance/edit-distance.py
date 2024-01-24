class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        nrow = len(word1)
        ncol = len(word2)
        # if not word1 or not word2:
        #     return len(word1) if word1 else len(word2)

        dp = [[0] * (ncol+1) for _ in range(nrow+1)]

        for i in range(1, nrow+1):
            dp[i][0] = i
        
        for j in range(1, ncol+1):
            dp[0][j] = j

        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else: 
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        print(dp)
        return dp[nrow][ncol]

            

            

            
