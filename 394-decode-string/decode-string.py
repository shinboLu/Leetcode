class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 

        for char in s:
            if char != ']':
                stack.append(char)
            if char == ']':
                cur_str = ''
                cur_count = ''
                while stack and stack[-1] != '[': 
                    cur_str = stack.pop() + cur_str
                stack.pop()
                while stack and stack[-1].isdigit():
                    cur_count = stack.pop() + cur_count
                
                stack.append(int(cur_count) * cur_str)
        return ''.join(stack)