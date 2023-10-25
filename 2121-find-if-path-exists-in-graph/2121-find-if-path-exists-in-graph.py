class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set([source])
        queue = collections.deque([source])

        while len(queue) > 0:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
        return False
        