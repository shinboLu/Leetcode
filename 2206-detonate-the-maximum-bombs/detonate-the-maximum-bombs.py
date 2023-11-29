class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi-xj) ** 2 + (yi-yj) ** 2:
                    adj_list[i].append(j)

        def dfs(curr, visited):
            visited.add(curr)
            for nei in adj_list[curr]:
                if nei not in visited:
                    dfs(nei, visited)
            return len(visited)

        res = 0
        

        for i in range(n):
            visited = set()
            res = max(res, dfs(i, visited))
        
        return res

