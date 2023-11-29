from heapq import heappop, heappush, heapify
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int: 
        graph = collections.defaultdict(list)
        for u, v, w in connections:
            graph[u].append((v, w))
            graph[v].append((u, w))

        hq = [(0, 1)] # cost, start city

        heapify(hq)
        visited =set()
        total_cost = 0

        while hq:
            cost, city = heappop(hq)
            if city not in visited:
                visited.add(city)
                total_cost += cost
                for next_city, next_cost in graph[city]:
                    heappush(hq, (next_cost, next_city))
        return total_cost if len(visited) == n else -1
