from heapq import heappop, heappush, heapify
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        for u, v, w in roads:
            graph[u-1].append((v-1, w))
            graph[v -1].append((u-1, w))

        ## store the min cost to get an apple from each vertex
        res = [float('inf')] * n
        ## start with each vertex
        for i in range(n):
            distance = [float('inf')] * n 
            ## each vertex is 0 because starting from itself
            distance[i] = 0
            pq = [(0,i)]
            while pq:
                w, cur_pos = heapq.heappop(pq)
                res[i] = min(res[i], appleCost[cur_pos] + (k+1) * w)
                for next_pos, next_w in graph[cur_pos]:
                    next_vertex_cost = w + next_w
                    if next_vertex_cost < distance[next_pos]:
                        distance[next_pos] = next_vertex_cost
                        heappush(pq, (next_vertex_cost, next_pos))

        return res



        