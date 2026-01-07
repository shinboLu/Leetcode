class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self, x):
        if self.root[x] == x:
            return x 
        self.root[x] = self.find(self.root[x])
        return self.root[x] 
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] +=1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c+1)
        for u, v in connections:
            uf.union(u, v)
        
        online = [True] * (c+1)
        offline_counts = [0] * (c+1)
        min_open = {}
        res = []
        for check, sid in queries:
            if check == 2:
                online[sid] = False
                offline_counts[sid]+=1

        for i in range(1, c+1):
            root=uf.find(i)
            if root not in min_open:
                min_open[root] = -1
            station = min_open[root]
            if online[i]:
                if station == -1 or station > i:
                    min_open[root] = i

        for i in range(len(queries)-1, -1, -1):
            check, sid = queries[i] 
            root = uf.find(sid) 
            station = min_open[root] 

            if check == 1:
                if online[sid]:
                    res.append(sid)
                else:
                    res.append(station)
            
            if check == 2:
                if offline_counts[sid] > 1:
                    offline_counts[sid] -=1
                else:
                    online[sid] = True
                    if station == -1 or station > sid:
                        min_open[root] = sid

        return res[::-1]

                