from heapq import heappush, heapify, heappop
class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v,w))
        if len(graph[s]) == 0:
            return -1

        
        hq = [(0, s)]
        heapify(hq)
        visited = set()

        distance = {x:float('inf') for x in range(n)}
        distance[s] = 0

        while hq:
            cost, dest = heappop(hq)
            visited.add(dest)
            for next_city, next_cost in graph[dest]:
                if next_city in visited:
                    continue
                if distance[next_city] > cost + next_cost:
                    distance[next_city] = cost + next_cost
                    heappush(hq, (cost + next_cost, next_city))

        res = float('inf')
        for node in marked:
            res = min(res, distance[node])

        return res if res !=float('inf') else -1