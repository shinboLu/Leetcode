class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(idx, comb):
            if idx == len(nums):
                res.append(comb.copy())
                return
            
            if idx > len(nums):
                return 
            
            comb.append(nums[idx])
            bt(idx+1, comb)
            comb.pop()
            bt(idx+1, comb)

        bt(0, [])
        return res


