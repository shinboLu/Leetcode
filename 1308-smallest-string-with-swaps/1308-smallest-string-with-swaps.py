from collections import deque
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
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
    def connected(self, x, y):
        return self.find(x) == self.find(y) 

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n = len(s)
        uf = unionFind(n)

        for x, y in pairs: 
            uf.union(x, y)

        
        group = collections.defaultdict(lambda: ([], []))

        for i, ch in enumerate(s):
            parent= uf.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)


        res = [''] * n
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch

        return "".join(res)


        

        