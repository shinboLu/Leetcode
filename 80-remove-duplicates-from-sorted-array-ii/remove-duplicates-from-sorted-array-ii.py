
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count= 1

        left = 1

        while left < len(nums):
            if nums[left] == nums[left-1]:
                count += 1
                if count > 2:
                    nums.pop(left)
                    left -= 1
            else:
                count = 1
            left += 1
        return left





        # left, count = 1, 1

        # while left <  len(nums):
        #     if nums[left] == nums[left-1]:
        #         count += 1
        #         if count > 2:
        #             nums.pop(left)
        #             left -= 1
        #     else:
        #         count = 1
        #     left += 1
        # return len(nums)

            


        