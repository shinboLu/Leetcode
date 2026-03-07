class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = [] 
        pre_op = '+'
        s+=pre_op
        cur = 0
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            else:
                if pre_op == '+':
                    stack.append(cur)
                elif pre_op == '-':
                    stack.append(-cur)
                elif pre_op == '*':
                    num = stack.pop()
                    stack.append(num * cur)
                elif pre_op == '/':
                    num = stack.pop()
                    stack.append(int(num/cur))
                cur = 0
                pre_op = char
        return sum(stack)



