class Solution:
    def numberCount(self, a: int, b: int) -> int:

        dp = [0] * (b+1)
        
        for i in range(a, b+1):
            # if i< 10:
            #     dp[i] = 1
            if len(set(str(i))) != len(str(i)):
                continue
            dp[i] = 1
        
        print(dp)

        return sum(dp)

            
