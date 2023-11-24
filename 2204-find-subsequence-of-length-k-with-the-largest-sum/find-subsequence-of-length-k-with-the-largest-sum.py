from heapq import heappush, heappop

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        counter = collections.Counter(heap)
        res = []
        for n in nums:
            if counter[n] > 0:
                counter[n] -=1
                res.append(n)

        return res
