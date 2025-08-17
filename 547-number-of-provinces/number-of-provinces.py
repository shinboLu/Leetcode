class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self,x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        res = n
        for i in range(n):
            for j in range(i+1, n):
                print(i,j)
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    res -=1 
                    uf.union(i,j)
        return res
                    

        