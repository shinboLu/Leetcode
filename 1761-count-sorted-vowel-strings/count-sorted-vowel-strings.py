class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        res = []
        def backtrack(index, combs):
            if len(combs) == n:
                res.append(''.join(combs))
                return 

            for i in range(index,len(vowels)):

                if vowels[i-1] <= vowels[i]:
                    combs.append(vowels[i])
                    backtrack(i, combs)                
                    combs.pop()

        backtrack(-1, [])


        return len(res)