from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start, dest, price in flights:
            graph[start].append((dest, price))

        
        visited = {}
        def dijkstra(graph, src, dst, k):
            miniheap = [(0, 0, src)]
            while miniheap:
                cost, stops, start = heappop(miniheap)
                visited[start] = stops

                if start == dst:
                    return cost
                
                if stops > k:
                    continue

                for next_city, next_cost in graph[start]:
                    if next_city not in visited or visited[next_city] > stops:
                        heapq.heappush(miniheap, (cost + next_cost, stops + 1, next_city))
            return -1
        return dijkstra(graph, src, dst, k)








        
        
