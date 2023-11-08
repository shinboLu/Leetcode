class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = []

        for currNode in range(n):
            for next_node in range(currNode + 1, n):
                weight = abs(points[currNode][0] - points[next_node][0]) + abs(points[currNode][1] - points[next_node][1])
                graph.append((weight, currNode, next_node))
        graph.sort(key= lambda x: x[0])
        #print(graph)
        uf= unionFind(n)
        mst_cost = 0
        edges_used = 0

        for weight, curr_node, next_node in graph:
            if uf.union(curr_node, next_node):
                mst_cost += weight
                edges_used += 1
                if edges_used == n -1:
                    break

        return mst_cost
