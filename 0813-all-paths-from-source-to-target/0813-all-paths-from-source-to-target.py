class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1

        res = []

        def backtracking(node, path):
            if node == n:
                res.append(list(path))
                return 

            for next_node in graph[node]:
                path.append(next_node)
                backtracking(next_node, path)
                path.pop()
        backtracking(0, [0])
        return res