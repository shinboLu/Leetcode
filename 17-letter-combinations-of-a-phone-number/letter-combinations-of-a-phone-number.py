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
        def backtracking(index, combs):
            if len(combs) == len(digits):
                res.append(''.join(combs))
                return
            cur_num = digits[index]

            for letter in graph[cur_num]:
                print(letter)
                combs.append(letter)
                print(combs)
                backtracking(index + 1, combs)
                combs.pop()
        backtracking(0, [])
        return res