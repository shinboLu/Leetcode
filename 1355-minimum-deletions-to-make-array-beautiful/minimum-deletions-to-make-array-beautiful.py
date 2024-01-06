class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        isEven = True
        for i in range(n):
            if isEven:
                if i % 2 == 0 and i != n -1 and nums[i] == nums[i+1]:
                    res += 1
                    isEven = False

            elif not isEven:
                if i % 2 == 1 and i !=n -1 and nums[i] == nums[i+1]:
                    res += 1
                    isEven = True
        curLen = n - res 
        return res if curLen % 2 == 0 else res + 1