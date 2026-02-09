class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mapping = collections.defaultdict(int)
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum == goal:
                count +=1
        
            if prefix_sum - goal in mapping:
                count += mapping[prefix_sum - goal] 
            
            mapping[prefix_sum] = mapping[prefix_sum] +1 

        return count
        

