from heapq import heappush, heappop, heapify
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        adj_matrix = collections.defaultdict(list) 

        for idx, val in enumerate(edges):
            adj_matrix[val].append(idx)
        
        heapq = []
        for key, val_list in adj_matrix.items():
            heappush(heapq, [-sum(val_list), key]) 
        
        return heappop(heapq)[1]
        
