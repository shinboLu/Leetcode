class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(left, right, combs):
            if len(combs) == n*2:
                res.append(''.join(combs.copy()))
                return

            if left < n:
                combs.append('(')
                bt(left+1, right, combs)
                combs.pop()
            if right < left:
                combs.append(')')
                bt(left, right+1, combs)
                combs.pop()
            

        bt(0,0,[])

        return res            