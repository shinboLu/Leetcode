class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = [] 

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        res = [] 

        for n, p in zip(neg, pos):
            res.append(p)
            res.append(n)

        return res