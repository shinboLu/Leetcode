class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        indegree = [0] * (n+1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        step = 0 
        studied = -1
        #print(studied)
        while queue:
            length = len(queue)
            for _ in range(length):
                cur_node = queue.popleft()
                studied += 1
                print(studied)
                for next_node in graph[cur_node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.append(next_node)
            step += 1

        return step if studied == n else -1
                
    