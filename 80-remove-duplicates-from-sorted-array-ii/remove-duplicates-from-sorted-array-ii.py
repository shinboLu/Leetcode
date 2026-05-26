class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 
        count=1
        for right in range(1, len(nums)):
            if nums[right] == nums[left]:
                if count < 2:
                    left +=1
                    nums[left] = nums[right]
                    count +=1
            else: 
                left +=1
                nums[left]= nums[right]
                count = 1
        return left+1
