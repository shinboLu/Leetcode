class UnionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
            
        res = collections.defaultdict(list)
        for email, owner in ownership.items():
            res[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]