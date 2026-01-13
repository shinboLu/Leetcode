class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}': '{',
            ')': '(',
            ']':'['
        }
        stack = [] 

        for char in s: 
            if char in pairs.values():
                stack.append(char) 
            elif not stack:
                return False
            elif pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return len(stack)==0

