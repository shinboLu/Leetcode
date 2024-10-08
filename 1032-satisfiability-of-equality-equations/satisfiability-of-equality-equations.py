class unionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x ):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.root[root_y]:
            self.root[root_x] = self.root[root_y]
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
        uf = unionFind(n)

        for equation in equations:
            if equation[1] == '=':
                x, y = ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a')
                uf.union(x, y)

        for equation in equations:
            if equation[1] == '!':
                x, y = ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False 
        
        return True 

        