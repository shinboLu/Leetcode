class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size
        self.component = size

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y or root_y != y :
            return False
        
        # if root_x != root_y:
        #     if self.rank[root_x] > self.rank[root_y]:
        #         self.root[root_y] = root_x
        #     elif self.rank[root_x] < self.rank[root_y]:
        #         self.root[root_x] = root_y
        #     else: 
        self.root[root_y] = root_x
        self.rank[root_x] += 1
        self.component -=1 
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = list(zip(leftChild, rightChild))
        uf = unionFind(n)

        for root in range(n):
            for child in [leftChild[root], rightChild[root]]:
                if child == -1:
                    continue
                
                if not uf.union(root, child):
                    return False
        return uf.component == 1 
                
                
