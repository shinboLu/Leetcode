class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s) 
        #memo = {} 

        @cache
        def dp(idx):
            if idx == n:
                return 0

            res = dp(idx+1) + 1
            
            for end in range(idx, n):
                cur = s[idx:end+1]
                if cur in dictionary:
                    res = min(res, dp(end+1))
            return res 
        return dp(0)