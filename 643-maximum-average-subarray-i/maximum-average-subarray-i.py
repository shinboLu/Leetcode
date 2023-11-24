class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        n = len(nums)
        curr_avg = sum(nums[:k])
        tot_max = curr_avg/k

        while i + k + 1 <= n:
            curr_avg -= nums[i]
            curr_avg += nums[i+k]

            if tot_max < curr_avg/k:
                tot_max = curr_avg / k

            i += 1

        return tot_max

            
