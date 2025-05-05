class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(v1,v2,o):
            if o == '+':
                return v1 + v2
            if o == '*':
                return v1 * v2
            if o == '/':
                return int(v1/v2)
            if o =='-':
                return v1-v2
        nums = []
        oper = ["+", '-', '*', '/']
        for token in tokens:
            if token not in oper:
                nums.append(token)
                continue
            
            if token in oper and len(nums) >=2:
                num1 = int(nums.pop())
                num2 = int(nums.pop())
                cur_res = calc(num2, num1, token)
                nums.append(int(cur_res))

        return int(nums.pop())


                    