class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #max_avg = float('-inf')
        first_k_sum = sum(nums[:k])
        max_avg = first_k_sum/k
        n = len(nums)

        left = 0

        while left + k + 1 <= n:
            first_k_sum += nums[left + k]
            first_k_sum -= nums[left]

            if max_avg < first_k_sum / k:
                max_avg = first_k_sum / k
            left += 1 
        return max_avg