class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size 

    def find(self, x):
        if self.root[x] == x:
            return x 
        self.root[x] = self.find(self.root[x])
        return self.root[x] 

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] =root_x
            self.rank[root_x] += 1
        return True 


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        uf = UnionFind(n)

        for x, y in edges:
            if not uf.union(x, y):
                return False
        return True