class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1 for _ in range(size)]

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
            self.rank[root_x] +=1
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n) 

        for s,e in edges:
            uf.union(s, e)
        
        if uf.isConnected(source, destination):
            return True
        return False