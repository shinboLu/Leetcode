class unionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1]*size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
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
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        vertices = [i for i in range(n)]
        size = [1] * n
        roots = {i for i in range(n)}
        res = 0
        uf = unionFind(n+1)
        for u, v in edges:
            uf.union(u,v)

        groups = collections.defaultdict(int)
        for i in range(n):
            groups[uf.find(i)] += 1

        nodes_seen = 0
        for group_cnt in groups.values():
            res += group_cnt * (n - group_cnt - nodes_seen)
            nodes_seen += group_cnt

        return res
        

        

