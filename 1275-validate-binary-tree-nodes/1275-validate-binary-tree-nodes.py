class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size
        self.ncomponent = size

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
        self.ncomponent -= 1
        self.root[root_y] = root_x

        return True
    
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = list(zip(leftChild, rightChild))
        uf = unionFind(n)
        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child == -1:
                    continue
                
                if not uf.union(node, child):
                    return False
        return uf.ncomponent == 1