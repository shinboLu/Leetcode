class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        if 0 in restricted:
            return 0
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        for node in restricted:
            visited[node] = True
        visited[0] = True

        queue = collections.deque()
        queue.append((0))
        count = 0
        while queue:
            curr_node = queue.popleft()
            count += 1
            for next_node in graph[curr_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
        return count 
        


