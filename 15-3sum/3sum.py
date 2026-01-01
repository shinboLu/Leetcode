class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def two_sum(i):
            left = i+1
            right = len(nums)-1

            while left < right:
                if nums[i]+nums[left]+nums[right]==0:
                    res.append((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right]==nums[right+1]:
                        right -=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1
                else:
                    right-=1
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            if i == 0 or nums[i] != nums[i-1]:
                two_sum(i)
        return res

