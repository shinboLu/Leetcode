class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        indegree = [0] * (n+1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        queue = collections.deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        semesters = 0 
        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                cur_class = queue.popleft()
                n -= 1
                for next_class in graph[cur_class]:
                    indegree[next_class] -= 1
                    if indegree[next_class] == 0:
                        queue.append(next_class)
            semesters += 1

        return semesters if n == 0 else -1


