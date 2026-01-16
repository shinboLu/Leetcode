class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix_sum.append(cur_sum)

        for i in range(1, len(nums)+1):
            if prefix_sum[-1] - prefix_sum[i-1] == prefix_sum[i]:
                return i -1

        return -1