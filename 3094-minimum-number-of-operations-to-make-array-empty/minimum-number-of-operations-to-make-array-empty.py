class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        print(counter.items())

        res = 0 

        for k, val in counter.items():
            if val == 1:
                return -1
            res += math.ceil(val / 3)

        return res