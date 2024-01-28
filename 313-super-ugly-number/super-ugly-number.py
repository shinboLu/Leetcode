class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res = [1]
        idx = [0] * len(primes)
        prod = [p for p in primes]

        while len(res) < n:
            next_ugly = min(prod)
            res.append(next_ugly)
            for i in range(len(primes)):
                if next_ugly == prod[i]:
                    idx[i] += 1
                    prod[i] = primes[i] * res[idx[i]] 

        return res[-1]
            