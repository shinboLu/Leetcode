class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2 
        n = len(nums)
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            cur_num = nums[i] 
            nextDp = set()
            for t in dp:
                nextDp.add(t)
                nextDp.add(t + cur_num)
            dp = nextDp
        return target in dp
                


                

                
                