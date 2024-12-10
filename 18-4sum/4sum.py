class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            if not nums:
                return res
            
            average_val = target//k

            if average_val < nums[0] or nums[-1] < average_val:
                return res
            
            if k == 2:
                return twoSum(nums,target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1 : ], target-nums[i], k - 1):
                        res.append([nums[i]]+ subset)
            return res

        def twoSum(nums, target):
            res = []
            left, right = 0, len(nums) - 1

            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum < target or (left > 0 and nums[left] == nums[left-1]):
                    left += 1
                elif cur_sum > target or (right < len(nums)-1 and nums[right] == nums[right] + 1):
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1 
                    right -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
