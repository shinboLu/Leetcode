class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # Build adjacency list.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Perform BFS to find distances.
        distance = [None] * len(patience)
        distance[0] = 0
        queue = deque()
        queue.append(0)
        # Instance of explicitly keeping track of which nodes are
        # visited, use None as the distance to unvisited nodes.
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not distance[neighbor]:
                    distance[neighbor] = 1 + distance[node]
                    queue.append(neighbor)

        def getLastSend(n: int) -> int:
            """Compute when the last message is sent by node n."""
            if patience[n] >= 2 * distance[n]:
                return 0
            if (2 * distance[n]) % patience[n] == 0:
                return 2 * distance[n] - patience[n]
            return 2 * distance[n] - (2 * distance[n] % patience[n])

        # Calculate the max time for a node to receive its last response.
        maxTime = 0
        for n in range(1, len(patience)):
            lastSend = getLastSend(n)
            lastReceive = lastSend + 2 * distance[n]
            maxTime = max(maxTime, lastReceive)
        # The above loop can be replaced by a single line with a list comprehension:
        maxTime = max(getLastSend(n) + 2 * distance[n] for n in range(1, len(patience)))

        return maxTime + 1