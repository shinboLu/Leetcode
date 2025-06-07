class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0

        left, right = 0, 0
        count = 0
        while right <= len(nums)-1:
            if nums[left] != nums[right]:
                left += 1 
                nums[left] = nums[right]

            elif left < right and count < 2:
                left += 1
                nums[left] = nums[right]
            right += 1
            count +=1 

            if right <= len(nums)-1 and nums[right]!= nums[right-1]:
                count = 0

        return left +1
        
        print(nums)
        return res 