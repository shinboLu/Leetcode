class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # m = len(vowels)

        # dp = [[0] * (m+1) for _ in range(n+1)]
        res = []
        def backtrack(index, combs):
            if len(combs) == n:
               # print(combs)
                res.append(''.join(combs))
                return 

            for i in range(index,len(vowels)):

                if vowels[i-1] <= vowels[i]:
                    combs.append(vowels[i])
                    #print(combs)
                    backtrack(i, combs)                
                    combs.pop()

        backtrack(-1, [])


        return len(res)