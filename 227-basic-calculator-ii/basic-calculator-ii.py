class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(' ', '')
        prev_op = '+'
        cur_num = 0
        s += prev_op

        for char in s:
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            else:
                if prev_op == '+':
                    stack.append(cur_num)
                elif prev_op == '-':
                    stack.append(-cur_num) 
                elif prev_op == '*':
                    stack.append(stack.pop() * cur_num)
                else:
                    stack.append(int(stack.pop()/cur_num))
                cur_num = 0 
                prev_op = char
        return sum(stack)
