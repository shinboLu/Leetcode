class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        res = [False] * len(graph)
        indegree = [0] * len(graph)
        queue = collections.deque()

        for i in range(len(graph)):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        print(adj)
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            terminal = queue.popleft()
            res[terminal] = True
            for nxt in adj[terminal]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        for i in range(len(res)):
            if res[i]:
                yield i



            

        
                
