class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')

        if not s:
            return 0

        idx, num, sign = 0, 0, 1

        if s[0] == '+':
            sign = 1
            idx+=1
        elif s[0] == '-':
            sign = -1 
            idx+=1

        while idx < len(s) and s[idx].isdigit():
            digit = int(s[idx])

            if num > (2 ** 31 -1 - digit)//10:
                return 2 ** 31-1 if sign == 1 else -2**31
            
            num = num * 10 + digit 
            idx += 1
        
        return sign * num 
