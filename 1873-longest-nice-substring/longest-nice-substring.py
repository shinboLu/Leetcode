class Solution:
    def longestNiceSubstring(self, s: str) -> str:


        def check(s):
            return len(set(s.lower())) == len(set(s))// 2

        
        window = len(s) 

        while window: 
            for i in range(len(s) - window + 1):
                sub = s[i : i + window]

                if check(sub):
                    return sub 
            
            window -= 1

        
        return ''
            