class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #graph = collections.defaultdict(list)
        in_nodes = collections.defaultdict(list)
        out_nodes = collections.defaultdict(list)

        for u, v in connections:
            in_nodes[v].append(u)
            out_nodes[u].append(v)

        visited = [0] * n
        visited[0] = 1
        queue = collections.deque()
        queue.append(0)
        steps = 0

        while queue:
            cur = queue.popleft()
            for i in in_nodes[cur]:
                if visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)
            for i in out_nodes[cur]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
                    steps += 1
        return steps
                

        
        


