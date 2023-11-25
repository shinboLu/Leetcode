class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v, cost in roads:
            graph[u-1].append((v-1, cost))
            graph[v-1].append((u-1,cost))

        cost_list = [float('inf')] * n

        for i in range(n):
            dist = [float('inf')] * n
            dist[i] = 0 
            pq = [(0,i)]
            while pq:
                d, u = heapq.heappop(pq)
                cost_list[i] = min(cost_list[i], appleCost[u] + (k + 1) * d)
                for v, w in graph[u]:
                    temp_d = d + w
                    if temp_d < dist[v]:
                        dist[v] = temp_d
                        heapq.heappush(pq, (temp_d, v))

        return cost_list

        

        