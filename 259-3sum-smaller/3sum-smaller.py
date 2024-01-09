class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum < target:
                    res += right - left

                    left += 1
                else:
                    right -= 1

        return res 