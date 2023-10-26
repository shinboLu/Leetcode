class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1

        res = []

        def backtracking(curr_node, path):
            if curr_node == n:
                res.append(list(path))
                return
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtracking(next_node, path)
                path.pop()

        path = [0]
        backtracking(0, path)
        return res          
            
        