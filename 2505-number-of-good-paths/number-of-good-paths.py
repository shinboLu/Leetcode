class unionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] == x:
            return x 
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return 
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x

            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        uf = unionFind(n)
        good_path = 0 
        adj_list = collections.defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        value_node_map = collections.defaultdict(list)
        for index, val in enumerate(vals):
            value_node_map[val].append(index)


        for value, nodes in sorted(value_node_map.items()): 
            for node in nodes: 
                for neig in adj_list[node]:
                    if vals[node] >= vals[neig]:
                        uf.union(node, neig)

            group = {}
            for node in nodes:
                group[uf.find(node)] = group.get(uf.find(node), 0) + 1

            for size in group.values():
                good_path += (size * (size + 1)) //2

        return good_path
