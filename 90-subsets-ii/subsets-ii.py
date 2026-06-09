class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        
        def bt(idx, combs): 
            if combs in res:
                return 
            
            res.append(combs.copy())

            for i in range(idx, len(nums)):
                combs.append(nums[i])
                bt(i+1, combs)
                combs.pop()
        bt(0, [])
        return res