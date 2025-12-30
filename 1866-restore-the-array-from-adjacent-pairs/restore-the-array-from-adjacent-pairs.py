class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for i, j in adjacentPairs:
            adj_list[i].append(j)
            adj_list[j].append(i)

        res = []
        visited = set() 

        def dfs(node):
            nonlocal res
            
            res.append(node)
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)
            return 

        root = None
        for num in adj_list:
            if len(adj_list[num]) == 1:
                root = num
                break
        dfs(root)
        return res



