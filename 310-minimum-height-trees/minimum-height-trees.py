class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adj_list = collections.defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        print(adj_list)
        leaves = collections.deque()
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)
        remaining_node = n
        while remaining_node > 2: 
            remaining_node -= len(leaves)
            next_level_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    next_level_leaves.append(neighbor)
            leaves = next_level_leaves

        return leaves


        