class unionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        is_mergered = False
        if root_x == root_y:
            return is_mergered
        is_mergered = True
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_x] += 1
        return is_mergered

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x : x[0])

        uf = unionFind(n)
        count = n

        for time, a, b in logs:
            if uf.union(a, b):
                count -= 1
            if count == 1:
                return time
        return -1