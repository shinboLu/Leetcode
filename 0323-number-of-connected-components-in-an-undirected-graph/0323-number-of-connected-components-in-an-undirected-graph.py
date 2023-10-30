class UnionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
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
            return 0
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_x] += 1
        return 1



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for x, y in edges:
            res -= uf.union(x,y)
        return res 