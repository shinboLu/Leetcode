class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.root = [i for i in range(n)] 
        self.components = n
    def find_root(self, x):
        if self.root[x] == x:
            return self.root[x]
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find_root(x) 
        rooty = self.find_root(y) 
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = self.root[x]
                self.rank[rootx]+=1
            self.components-=1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        nrow = len(isConnected)
        ncol = len(isConnected[0])

        for row in range(nrow):
            for col in range(ncol):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        
        return uf.components