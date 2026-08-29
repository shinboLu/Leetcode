class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1_idx = len(num1)-1
        n2_idx = len(num2)-1
        carry = 0 
        res = []

        while n1_idx >= 0 or n2_idx >= 0:
            n1_d = ord(num1[n1_idx]) - ord('0') if n1_idx >= 0 else 0 
            n2_d = ord(num2[n2_idx]) - ord('0') if n2_idx >= 0 else 0
            
            cur = (carry+n1_d+n2_d) % 10
            carry = (carry+n1_d+n2_d)//10

            res.append(cur) 
            n1_idx-=1
            n2_idx-=1
        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])
