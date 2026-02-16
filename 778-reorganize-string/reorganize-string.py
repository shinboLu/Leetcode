from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        pq = [(-count, char) for char, count in counter.items()] 
        heapify(pq)
        prev_count, prev_char = 0, ''

        res = []
        start = 0
        while pq:
            count, char = heappop(pq)
            res.append(char)
            count +=1
            if prev_count < 0:
                heappush(pq, (prev_count, prev_char))
            prev_count, prev_char = count, char

        return ''.join(res) if len(res) == len(s) else ''