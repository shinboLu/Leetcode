class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        roots = [x ** 2 for x in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')]* (n+1)
        dp[0] = 0


        for i in range(1, n+1):
            for j in roots:
                if i < j:
                    break  
                dp[i] = min(dp[i], dp[i-j] + 1)

        return dp[-1]
