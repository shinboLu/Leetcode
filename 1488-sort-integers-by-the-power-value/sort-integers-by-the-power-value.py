class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = [] 
        nums = [x for x in range(lo, hi+1)]
        for i in range(lo, hi+1):
            count = 0 
            while i > 1:
                if i % 2 == 0:
                    i //= 2 
                else:
                    i = 3 * i + 1
                count += 1
            powers.append(count)

        return [x for _, x in sorted(zip(powers, nums))][k-1]
        