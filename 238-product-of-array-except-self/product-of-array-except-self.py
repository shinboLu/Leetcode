class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n
        res = []

        for i in range(n-1):
            left_prod[i+1] = nums[i] * left_prod[i]

        for i in range(n-1, 0, -1):
            right_prod[i-1] = nums[i] * right_prod[i]

        for i in range(n):
            res.append(left_prod[i] * right_prod[i])


        return res 