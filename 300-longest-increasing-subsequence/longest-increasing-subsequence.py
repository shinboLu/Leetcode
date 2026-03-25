class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            left = bisect.bisect_left(res, num)
            if left == len(res):
                res.append(num)
            else:
                res[left] = num

        return len(res)

