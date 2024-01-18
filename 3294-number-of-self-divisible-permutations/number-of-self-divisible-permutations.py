class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        if n == 1:
            return 1
        res = 0 

        def backtrack(index, combs):
            nonlocal res 
            if len(combs) == n:
                res += 1

            else:
                for i in range(1, n+1):
                    if i not in combs and gcd(i, index) == 1:
                        backtrack(index + 1, combs + [i])

        backtrack(1, [])
        return res 