class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums) 
        special = n-2
        tot_sum = sum(nums)
        counter = collections.Counter(nums)

        res = float('-inf')

        for num in counter.keys():
            outlier_cand = tot_sum - 2 * num

            if outlier_cand in counter:
                if outlier_cand != num or counter[outlier_cand] > 1:
                    res = max(outlier_cand, res)
        return res
