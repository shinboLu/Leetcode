class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] 
        graph = {
            '2': ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def bt(idx, combs):
            if idx == len(digits):
                res.append(''.join(combs))
                return 

            cur_num = digits[idx]

            for d in graph[cur_num]:
                combs.append(d)
                bt(idx+1, combs)
                combs.pop()
        bt(0, [])

        return res 
            