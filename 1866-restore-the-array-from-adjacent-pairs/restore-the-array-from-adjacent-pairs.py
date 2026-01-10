class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacentPairs.sort(key=lambda x:x[0])
        res = []
        adj_list = collections.defaultdict(list) 
        visited = set()
        for u, v in adjacentPairs:
            adj_list[u].append(v)   
            adj_list[v].append(u)

        print(adj_list)

        def dfs(num):
            nonlocal res, visited

            visited.add(num) 
            res.append(num)

            for val in adj_list[num]:
                if val not in visited:
                    dfs(val)
        start = None
        for num in adj_list.keys():
            if len(adj_list[num]) == 1:
                start = num
                break
        print(start)
        dfs(start)
        return res

