class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(num0, num1, oper):
            if oper == '*':
                return num0 * num1
            elif oper == '+':
                return num0 + num1
            elif oper == '-':
                return num1 - num0
            else:
                return int(num1/num0)

        opers = ['*', '+', '-', '/']

        nums = [] 

        for tok in tokens:
            if tok not in opers:
                nums.append(tok)
            else:
                num1 = int(nums.pop())
                num0 = int(nums.pop())
                cur = calc(num1, num0, tok)
                nums.append(cur) 

        return int(nums[-1])