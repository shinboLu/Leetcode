class unionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return 
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        size = n + 1
        minScore = float('inf')

        uf = unionFind(size)

        for road in roads:
            uf.union(road[0], road[1])
        
        for road in roads:
            root1 = uf.find(1)
            root_x = uf.find(road[0])
            root_y = uf.find(road[1])
            if root1 == root_x == root_y:
                minScore = min(minScore, road[2])
        return minScore