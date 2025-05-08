class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        pairs = {
            "}":"{",
            "]":"[",
            ")": "("
            }

        stack = [] 

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

                    