class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = collections.defaultdict(list)
        blue_graph = collections.defaultdict(list)


        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        res = [-1 for i in range(n)]
        res[0] = 0
        queue = collections.deque()
        queue.append([0,0,None]) ## node, length, prev-edge-color
        visited = set()
        visited.add((0,None))

        while queue:
            node, length, prev_color = queue.popleft()
            if res[node] == -1:
                res[node] = length
            
            if prev_color != "RED":
                for nei in red_graph[node]:
                    if (nei, "RED") not in visited:
                        visited.add((nei, "RED"))
                        queue.append([nei, length+1, "RED"])
            if prev_color != "BLUE":
                for nei in blue_graph[node]:
                    if (nei, "BLUE") not in visited:
                        visited.add((nei, "BLUE"))
                        queue.append((nei, length + 1, "BLUE"))

        return res 
