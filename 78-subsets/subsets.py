class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## unique

        res = []
        
        def bt(index, comb):
            res.append(comb.copy())

            for i in range(index, len(nums)):
                comb.append(nums[i])
                bt(i+1, comb)
                comb.pop()

        bt(0, [])
        return res

            