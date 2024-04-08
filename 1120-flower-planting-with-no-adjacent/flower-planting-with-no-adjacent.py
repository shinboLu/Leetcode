class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        lookup = [1] * (n+1)
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)
            if lookup[u] == lookup[v]:
                possible = [1,2,3,4]
                for garden in adj[u]:
                    if lookup[garden] in possible:
                        possible.remove(lookup[garden])
                    
                lookup[u] = possible[0]

        return lookup[1:]


        