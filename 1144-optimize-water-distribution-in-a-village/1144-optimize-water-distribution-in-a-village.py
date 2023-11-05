class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size+1)]
        self.rank = [1] * (size+1)
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False            
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        total_cost = 0
        uf = unionFind(n)
        for idx, well_cost in enumerate(wells):
            ordered_edges.append((well_cost, 0, idx + 1))

        for house1, house2, pipe_cost in pipes:
            ordered_edges.append((pipe_cost, house1, house2))

        
        ordered_edges.sort(key = lambda x: x[0])

        for weight, house1, house2 in ordered_edges:
            if uf.union(house1, house2):
                total_cost += weight
        
        return total_cost







