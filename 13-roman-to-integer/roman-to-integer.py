class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        start = 0 
        res = 0 
        while start < len(s):
            if start < len(s)-1 and symbol[s[start]] < symbol[s[start+1]]:
                res += symbol[s[start+1]]-symbol[s[start]]
                start+=2
            else: 
                res += symbol[s[start]]
                start += 1
        return res