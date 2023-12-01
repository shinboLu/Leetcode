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

        def backtracking_update_combination(start,path):
            if start == len(digits):
                res.append(''.join(path))
                return

            next_digit = digits[start]

            for letter in graph[next_digit]:
                path.append(letter)
                backtracking_update_combination(start+1, path)
                path.pop()

        backtracking_update_combination(0, [])
        return res


