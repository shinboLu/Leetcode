class Solution:
    def __init__(self, w: List[int]):
        self.prefix_w = []
        cur_sum = 0
        for el in w:
            cur_sum += el
            self.prefix_w.append(cur_sum)
        self.total = sum(w)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        left = 0 
        right = len(self.prefix_w)-1 
        while left <= right:
            mid = (left+right)//2 
            if self.prefix_w[mid] >= target:
                right = mid -1
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()