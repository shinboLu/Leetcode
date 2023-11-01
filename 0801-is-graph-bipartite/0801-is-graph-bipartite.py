class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
             return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = unionFind(len(graph))
        for idx, row in enumerate(graph):
            for next in row:
                if uf.find(idx) == uf.find(next):
                    return False
            for entry in row[1:]:
                uf.union(row[0], entry)
        return True