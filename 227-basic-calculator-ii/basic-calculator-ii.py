class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(" ", "")
        cur_val = 0
        prev_op = '+'
        s += prev_op
        for char in s:
            if char.isdigit():
                cur_val = cur_val * 10 + int(char)
            else:
                if prev_op == '*':
                    prev_val = stack.pop()
                    stack.append(cur_val * prev_val)
                elif prev_op == '/':
                    prev_val = stack.pop()
                    stack.append(int(prev_val/cur_val)) 
                elif prev_op == '-':
                    stack.append(-cur_val)
                else:
                    stack.append(cur_val)
                cur_val = 0 
                prev_op = char
        return sum(stack)
