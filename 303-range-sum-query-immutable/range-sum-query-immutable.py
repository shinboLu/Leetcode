class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        cur_sum = 0
        self.prefix_sum = collections.defaultdict(int)
        self.prefix_sum[0]=0
        for idx, num in enumerate(nums):
            cur_sum += num
            self.prefix_sum[idx+1] = cur_sum


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)