class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s: 
            if c != ']':
                stack.append(c)
            else:
                cur_str = '' 
                cur_count = ''

                while stack and stack[-1] != '[':
                    cur_str = stack.pop() + cur_str
                stack.pop()

                while stack and stack[-1].isnumeric():
                    cur_count = stack.pop() + cur_count
                
                stack.append(int(cur_count) * cur_str)
        return ''.join(stack)