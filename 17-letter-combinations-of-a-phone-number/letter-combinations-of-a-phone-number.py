class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':'abc',
            '3':'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7':'pqrs',
            '8': 'tuv',
            '9':'wxyz'
        }

        res = [] 

        def bt(idx, combs):
            nonlocal res
            if idx == len(digits):
                res.append(''.join(combs.copy()))
                return 

            for char in mapping[digits[idx]]:
                combs.append(char)
                bt(idx+1, combs)
                combs.pop()

        bt(0, [])
        return res