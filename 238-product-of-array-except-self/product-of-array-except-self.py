class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]

        res = []

        for i in range(len(nums)-1):
            left[i+1] = nums[i] * left[i]
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = nums[i] * right[i]

        for i in range(len(nums)):
            cur = left[i] * right[i]
            res.append(cur)
        return res


