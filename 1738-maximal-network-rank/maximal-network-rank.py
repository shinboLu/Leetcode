class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        max_rank = 0 
        indegree = [0] * n
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        for c1 in range(n):
            for c2 in range(c1+1, n):
                curr_rank = len(graph[c1]) + len(graph[c2])
                if c2 in graph[c1]:
                    curr_rank -= 1
                max_rank = max(max_rank, curr_rank)

        return max_rank

        

        