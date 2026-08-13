class UnionFind:
    def __init__(self, n):
        self.rank = [1]*n
        self.root = [i for i in range(n)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x] 

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y) 

        if rootx == rooty:
            return
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = self.root[x]
            self.rank[rootx] +=1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        ownership = collections.defaultdict(int)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in ownership:
                    ownership[email] = i
                else:
                    uf.union(i, ownership[email])
        res = collections.defaultdict(list)

        for email, owner in ownership.items():
            res[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(email) for i, email in res.items()]
        