class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        ncol = len(vowels)
        dp = [[0] * (ncol+1) for _ in range(n+1)]

        for i in range(1, ncol+1):
            dp[1][i] = i
        
        for j in range(1, n+1):
            dp[j][1] = 1


        for i in range(2, n+1):
            for j in range(2, ncol+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

