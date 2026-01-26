class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for val in num:
            while k and stack and stack[-1] > val:
                stack.pop()
                k-=1
            stack.append(val)

        final = stack[:-k] if k else stack

        return ''.join(final).lstrip('0') or '0'