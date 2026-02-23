from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        vals = [-x for x in nums]
        heapify(vals)
       

        for i in range(k):
            cur = heappop(vals)
            if i == k-1:
                return -cur