class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for num in nums:
            if num > 0: 
                pos.append(num)
            else:
                neg.append(num)

        res = []
        for pos_int, neg_int in zip(pos,neg):
            res.append(pos_int)
            res.append(neg_int)

        return res