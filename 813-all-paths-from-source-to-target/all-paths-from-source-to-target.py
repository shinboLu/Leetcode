class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) -1

        def backtracking(node, path):
            if node == target:
                res.append(path.copy())
                return

            for next_node in graph[node]:
                path.append(next_node)
                backtracking(next_node, path)
                path.pop()

        backtracking(0, [0])
        return res
