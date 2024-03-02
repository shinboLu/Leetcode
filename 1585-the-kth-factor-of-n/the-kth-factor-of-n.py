from heapq import heappush, heappop
class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        def heappush_k(num):
            heappush(heap, -num) 
            if len(heap) > k:
                heappop(heap)  

        heap = []

        for x in range(1, int(n**0.5)+1):
            if n % x == 0:
                heappush_k(x) 
                if x != n // x:
                    heappush_k(n//x)
        return -heappop(heap) if k == len(heap) else -1 