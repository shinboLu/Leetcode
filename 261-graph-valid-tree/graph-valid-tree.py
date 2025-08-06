class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for in_node, out_node in edges:
            graph[in_node].append(out_node)
            graph[out_node].append(in_node)

        def bfs(n, edges, graph):
            queue = collections.deque([0])
            visited = set()

            parent = {}

            while queue:
                cur = queue.popleft()
                visited.add(cur)
                for child in graph[cur]:
                    if parent.get(cur) == child:
                        continue
                    if child in visited:
                        return False
                    parent[child] = cur
                    queue.append(child)
            return len(visited)==n
        return bfs(n, edges, graph)