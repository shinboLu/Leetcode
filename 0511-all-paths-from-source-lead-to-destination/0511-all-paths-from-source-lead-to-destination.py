class Solution:
    gray = 1
    black = 2
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def buildGraph(n, edges):
            graph = [[]for _ in range(n)]
            for edge in edges:
                graph[edge[0]].append(edge[1])

            return graph

        def dfs(graph, node, dest, states):
            if states[node] != None:
                return states[node] == Solution.black

            if len(graph[node]) == 0:
                return node == dest

            states[node] = Solution.gray

            for next_node in graph[node]:
                if not dfs(graph, next_node, dest, states):
                    return False
            
            states[node] = Solution.black
            return True
        graph = buildGraph(n, edges)
        return dfs(graph, source, destination, [None] * n )

        