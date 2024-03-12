class unionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size 
    
    def find(self, x):
        if self.root[x] == x:
            return x 

        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x) 
        rooty = self.find(y)

        if rootx == rooty:
            return 0
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rootx] += 1
        return 1 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = unionFind(n) 
        res = n 

        for u, v in edges:
            res -= uf.union(u,v)

        return res         