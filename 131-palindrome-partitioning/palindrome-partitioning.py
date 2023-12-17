class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isValid(comb):
            return comb == comb[::-1]

        def backtrack(index, combs):
            if index == len(s):
                res.append(combs.copy())
                return 

            for i in range(index+1, len(s)+1):
                next_string = s[index:i]
                print(next_string)
                if isValid(next_string):
                    backtrack(i, combs + [next_string])

        backtrack(0,[])
        return res
