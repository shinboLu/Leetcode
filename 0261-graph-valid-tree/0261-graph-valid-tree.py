class DSU:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        else: 
            self.root[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        return True
            


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        uf = DSU(n)

        for A, B in edges:
            if not uf.union(A,B):
                return False
        return True


