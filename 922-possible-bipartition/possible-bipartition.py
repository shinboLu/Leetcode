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
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y
                self.rank[root_x] += 1
            

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        uf = unionFind(n+1)
        adj_list = collections.defaultdict(list)
        for u, v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)
        
        for i in range(1, n + 1):
            for nei in adj_list[i]:
                if uf.find(i) == uf.find(nei):
                    return False
                uf.union(adj_list[i][0], nei)

        return True
            


        