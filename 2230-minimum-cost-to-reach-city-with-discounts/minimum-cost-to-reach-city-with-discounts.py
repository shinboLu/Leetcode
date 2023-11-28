from heapq import heappush, heappop, heapify 
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, toll in highways:
            graph[u].append((v, toll))
            graph[v].append((u, toll))

        cost = {(k,c): float('inf') for k in range(discounts+1) for c in range(n)}
        queue = []
        queue.append((0,discounts,0))
        heapify(queue)

        while queue:
            toll, discount, city = heappop(queue)
            if city == n - 1:
                return toll
            for v, t in graph[city]:
                if toll + t < cost[(discount, v)]:
                    cost[(discount, v)] = toll + t
                    heappush(queue, (cost[(discount,v)], discount, v))
                
                if discount and toll + t // 2 < cost[(discount-1, v)]:
                    cost[(discount-1, v)] = toll + t // 2
                    heapq.heappush(queue, (cost[(discount - 1, v)], discount - 1, v))
        return -1
