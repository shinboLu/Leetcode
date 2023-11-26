from heapq import heappush, heappop
from collections import deque, defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def helper(node):

            distance = [float('inf')]*n
            distance[node] = 0
            heap = []
            heappush(heap,(0,node))
            
            while heap:
                dist,node = heappop(heap)
                for nbr,d in graph[node]:
                    if dist+d < distance[nbr] and dist+d <= distanceThreshold:
                        distance[nbr] = dist+d
                        heappush(heap, (dist+d,nbr))
            
            res = -1
            for d in distance:
                res+= d<=distanceThreshold
            return res

        
        graph = defaultdict(list)
        for i,j,d in edges:
            graph[i].append((j,d))
            graph[j].append((i,d))
        
        no_nodes = float('inf')
        res = 0
        for node in range(n):
            x = helper(node)
            if x <= no_nodes:
                no_nodes = x
                res = node

        return res        