class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        
        def bt(node, path):
            if node == target:
                res.append(path.copy())
                return 

            for nxt in graph[node]:
                path.append(nxt)
                bt(nxt, path)
                path.pop()

        bt(0, [0])

        return res 
            


