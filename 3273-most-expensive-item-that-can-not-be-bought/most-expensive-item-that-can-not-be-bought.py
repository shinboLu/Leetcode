class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        limit = primeOne * primeTwo
        dp = [True] * (limit+1)
        res = 0
        for i in range(1, limit+1):
            if i < primeOne or i < primeTwo:
                if i % primeOne != 0 and i % primeTwo != 0:
                    dp[i] = False
            else:
                dp[i] = dp[i-primeOne] or dp[i-primeTwo]

        for idx, value in enumerate(dp):
            if value == False:
                res = idx

        return res