class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = math.ceil(len(nums) / 2)

        counter = collections.Counter(nums)

        for i, v in counter.items():
            if v >= limit:
                return i
