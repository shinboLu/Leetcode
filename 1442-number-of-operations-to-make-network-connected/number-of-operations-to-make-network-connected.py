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
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1 

        uf = unionFind(n)
        for u, v in connections:
            uf.union(u, v)

        count = 0 
        for i in range(n):
            if uf.find(i) == i:
                count += 1
        return count-1

