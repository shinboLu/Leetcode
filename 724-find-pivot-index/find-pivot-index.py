class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] 
        cur_sum = 0

        for num in nums:
            cur_sum += num
            prefix.append(cur_sum)

        for i in range(1, len(nums)+1):
            if cur_sum - prefix[i] == prefix[i-1]:
                return i-1


        return -1            
            
