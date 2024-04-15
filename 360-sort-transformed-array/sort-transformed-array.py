class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        for n in nums:
            mult = a * (n**2) + b * n + c

            res.append(mult)
        return sorted(res)
