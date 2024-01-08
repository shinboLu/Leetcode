class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return set(nums)
        res = []
        counter = collections.Counter(nums)
        limit = len(nums)//3
        print(limit)

        for k, v in counter.items():
            print(k, v)
            if v > limit:
                res.append(k)

        return res

