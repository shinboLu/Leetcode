class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 

        def bt(left_count, right_count, combs):
            if len(combs)== n * 2:
                res.append(''.join(combs))
                return 

            if left_count < n:
                combs.append('(')
                bt(left_count+1, right_count, combs)
                combs.pop()

            if right_count < left_count:
                combs.append(')')
                bt(left_count, right_count+1, combs)
                combs.pop()

        bt(0, 0, [])
        return res 
                

            