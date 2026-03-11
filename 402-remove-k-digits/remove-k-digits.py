class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        left = 0 
        right = 0 

        for val in num: 
            while stack and stack[-1] > val and k > 0:
                stack.pop()
                k-=1
            stack.append(val)
        while stack and k >0:
            stack.pop()
            k-=1
        return ''.join(stack).lstrip('0') or '0'