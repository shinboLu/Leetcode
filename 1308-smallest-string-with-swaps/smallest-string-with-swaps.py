class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x] 
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] +=1
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
        
class Solution: 
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s) 
        uf = UnionFind(n)
        s_li = [char for char in s]
        res = float(inf)

        for idx1, idx2 in pairs:
            uf.union(idx1, idx2)
        
        group = collections.defaultdict(lambda: ([], []))

        for i, ch in enumerate(s):
            parent = uf.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch) 
        res = [''] * n
        for idx, chars in group.values():
            idx.sort()
            chars.sort()
            for ch, i in zip(chars,idx):
                res[i] = ch
        return "".join(res)