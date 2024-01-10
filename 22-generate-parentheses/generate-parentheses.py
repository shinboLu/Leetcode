class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        size = n * 2

        def backtrack(left, right, combs):
            if left == right == n:
                res.append(''.join(combs))
                return
            
            if left < n:
                combs.append('(')
                backtrack(left+1, right, combs)
                combs.pop()

            if right < left:
                combs.append(')')
                backtrack(left, right +1, combs)
                combs.pop()

        backtrack(0, 0, [])

        return res 
