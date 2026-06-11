class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if self.root[x] == x:
            return self.root[x] 
        self.root[x] = self.find(self.root[x])
        return self.root[x] 

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y) 

        if rootx == rooty:
            return 
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] +=1 
        self.count-=1
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n) 
        for t, f1, f2 in logs:
            if uf.find(f1) != uf.find(f2):
                uf.union(f1, f2) 
                if uf.count == 1:
                    return t 
        return -1
