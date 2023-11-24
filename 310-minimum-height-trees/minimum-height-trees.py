class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]

        adj_list = collections.defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        ## starting from the leaves
        leaves = collections.deque()
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)
        ## "peeling the adj_list, untill the centroids are left"
        while n > 2:
            ## update the remaining nodes
            n -= len(leaves)
            next_level_leaves = []

            while leaves:
                curr_leaves = leaves.pop()
                ## get and remove the leaf connected to the current level of leaves
                neigh = adj_list[curr_leaves].pop()
                ## remove the current node from the connected leaf
                adj_list[neigh].remove(curr_leaves)
                if len(adj_list[neigh]) == 1:
                    next_level_leaves.append(neigh)
                
            leaves = next_level_leaves

        return leaves

