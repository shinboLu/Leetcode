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
        res= []
        def bt(idx, comb):
            nonlocal res, mapping 
            if len(comb) == len(digits):
                res.append(''.join(comb.copy()))
                return

            for num in mapping[digits[idx]]:
                comb.append(num) 
                bt(idx+1, comb)
                comb.pop()

        bt(0, [])
        return res