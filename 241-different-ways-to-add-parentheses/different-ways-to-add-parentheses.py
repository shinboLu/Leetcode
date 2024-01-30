class Solution:
    def isOperator(self, ch):
        return ch == '+' or ch == '-' or ch == '*'

    def getDiffWays(self, i, j, expression):
        res = []
        if j - i + 1 <= 2:
            res.append(int(expression[i:j+1]))
            return res

        for idx in range(i, j+1):
            if self.isOperator(expression[idx]):
                op = expression[idx]
                left = self.getDiffWays(i, idx -1, expression)
                right = self.getDiffWays(idx+1, j, expression)

                for l in left:
                    for r in right:
                        if op == '+':
                            res.append(l+r) 
                        elif op == '-':
                            res.append(l-r) 
                        elif op == '*':
                            res.append(l*r) 
        return res


    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression) 

        return self.getDiffWays(0, n-1, expression) 



