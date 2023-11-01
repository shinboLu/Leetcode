class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
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
            return 0

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
        return 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = unionFind(n)
        max_row, max_col = 0,0
        rows, cols = {}, {}
        removed = 0
        for idx, (row, col) in enumerate(stones):
            if row in rows:
                removed += uf.union(idx, rows[row])
            else:
                rows[row] = idx
            
            if col in cols:
                removed += uf.union(idx, cols[col])
            else:
                cols[col] = idx
        return removed
            

        



