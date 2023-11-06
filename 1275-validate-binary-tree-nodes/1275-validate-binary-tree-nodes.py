class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.ncomponents = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y or root_y != y:
            return False
        self.ncomponents -= 1
        self.root[root_y] = root_x
        return True
    
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = unionFind(n)
        graph = list(zip(leftChild, rightChild))
        for row, rows in enumerate(graph):
            for col, cols in enumerate(rows):
                if cols == -1:
                    continue
                if not uf.union(row, cols):
                    return False

        return uf.ncomponents == 1