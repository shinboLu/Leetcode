class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def find_two_sum(i): 
            nonlocal res
            left = i +1 
            right = len(nums)-1 

            while left < right:
                cur = nums[left]+nums[right]+nums[i]
                if cur < 0:
                    left +=1
                elif cur > 0:
                    right -=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                find_two_sum(i)
        return res