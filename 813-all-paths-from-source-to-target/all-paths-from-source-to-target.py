class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        visited = [False] * len(graph)
        def backtrack(cur, path):
            if cur == target:
                res.append(path.copy())
                return 
            visited[cur] = True

            for nei in graph[cur]:
                if visited[nei] == False:
                    path.append(nei)
                    backtrack(nei, path)
                    visited[nei] = False
                    path.pop()
            return 
        backtrack(0, [0])
        return res




