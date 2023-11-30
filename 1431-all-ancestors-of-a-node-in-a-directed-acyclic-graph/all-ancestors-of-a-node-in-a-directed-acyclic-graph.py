class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = collections.defaultdict(list)
        res = [set() for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            res[v].add(u)
            indegree[v] += 1

        queue = collections.deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_node = queue.popleft()
            for child_node in adj_list[curr_node]:
                res[child_node].update(res[curr_node])
                indegree[child_node] -= 1
                if indegree[child_node] == 0:
                    queue.append(child_node)

        return [sorted(s) for s in res]


