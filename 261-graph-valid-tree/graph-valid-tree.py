class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1 for x in range(size)]
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
    def is_connected(self, x,y):
        return self.find(x) == self.find(y)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        uf = UnionFind(n)

        for n1, n2 in edges:
            # if already connected, we found a cycle
            if uf.is_connected(n1, n2):
                return False
            uf.union(n1, n2)
        
        return True