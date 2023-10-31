class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y ):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)+1
        uf = unionFind(n)

        for a, b in edges:
            if uf.union(a,b) is False: 
                return [a,b]


        


            