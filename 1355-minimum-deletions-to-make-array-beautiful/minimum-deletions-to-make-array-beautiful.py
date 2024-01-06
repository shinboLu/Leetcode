class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        isEven = True
        res = 0

        for i in range(n-1):
            if isEven:
                if i % 2 == 0  and nums[i] == nums[i+1]:
                    res += 1
                    isEven = False

            elif not isEven:
                if i % 2 == 1 and nums[i] == nums[i+1]  :
                    res += 1
                    isEven = True
        cur_len = n - res
        return res if cur_len % 2 ==0 else res + 1