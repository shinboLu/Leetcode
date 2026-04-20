class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(idx, cur_comb):
            res.append(cur_comb.copy())

            for i in range(idx, len(nums)):
                cur_comb.append(nums[i])
                bt(i+1, cur_comb)
                cur_comb.pop()
                    
        bt(0, [])
        return res
         

