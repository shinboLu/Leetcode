from heapq import heappop, heappush, heapify 
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        
        hq = []
        for key,v in counter.items():
            hq.append([-v, key])
        heapify(hq)
        res = []
        while k > 0:
            v, key = heappop(hq)
            res.append(key) 
            k-=1

        return res
