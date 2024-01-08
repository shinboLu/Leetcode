class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break 

            if i == 0 or nums[i-1] != nums[i]:
                self.find2Sum(nums, res, i)
        return res
    def find2Sum(self, nums, res, i):
        left,right = i+1, len(nums) -1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            
            if cur_sum < 0:
                left += 1
            elif cur_sum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1

            
