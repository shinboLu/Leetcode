class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = {}
        
        for num in nums:
            if num == 0:
                continue 
            
            if num not in counter:
                counter[num] = 0
            
            counter[num] += 1
        
        print(counter)
        
        subtracts = list(counter.values())
        subtracts.sort()
        res = 0 
        while sum(subtracts) > 0:
            for i in range(len(subtracts)):
                subtracts[i] -= subtracts[i] 
                res += 1 
        return res 

