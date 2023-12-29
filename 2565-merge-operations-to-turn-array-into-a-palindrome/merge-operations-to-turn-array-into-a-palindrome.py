class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        res = 0 

        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                if nums[left] + nums[left+1] < nums[right] + nums[right-1]:
                    nums[left+1] += nums[left]
                    left += 1
                else:
                    nums[right-1] += nums[right]

                    right -= 1
                res += 1

        return res 

