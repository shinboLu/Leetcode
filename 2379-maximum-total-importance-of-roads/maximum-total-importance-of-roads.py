from heapq import heapify, heappop, heappush 
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [0] * n

        for u, v in roads:
            graph[u] += 1
            graph[v] += 1
        
        graph.sort()
        print(graph)
        total = 0 
        for i in range(len(graph)):
            total += graph[i] * (i+1)


        return total