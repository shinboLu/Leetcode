class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # steps = n - (k % n)
        steps = k % n
        print(steps)
        while steps > 0:
            first = nums.pop(-1)
            nums.insert(0, first)
            steps -=1