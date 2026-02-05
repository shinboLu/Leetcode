class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        pre_op = '+'
        s+='+'
        stack = []
        cur_eval = 0

        for char in s:
            if char.isdigit():
                cur_eval = cur_eval * 10 + int(char)
            else:
                if pre_op == '+':
                    stack.append(cur_eval)
                elif pre_op =='-':
                    stack.append(-cur_eval)
                elif pre_op =='*':
                    num = stack.pop()
                    stack.append(num*cur_eval)
                elif pre_op == "/":
                    num = stack.pop()
                    stack.append(int(num / cur_eval))
                cur_eval = 0 
                pre_op = char
        return sum(stack)

