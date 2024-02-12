class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        idx = 0
        res = 0

        while idx < len(s):
            if idx+1 < len(s) and dic[s[idx]] < dic[s[idx+1]]:
                res += dic[s[idx+1]] - dic[s[idx]]
                idx += 2
            else:
                res += dic[s[idx]]
                idx+=1
        return res