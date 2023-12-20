class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        choices = ['a', 'b', 'c']

        def backtrack(index, combs):
            if len(combs) == n:
                res.append(combs)
                return 

            for i in range(len(choices)):
                letter = choices[i]
                if len(combs) == 0:
                    backtrack(i, combs + letter)
                else:
                    if combs[-1] != letter:
                        backtrack(i, combs + letter)

        backtrack(0, '')
        
        if k <= len(res):
            return res[k-1]
        else:
            return ''