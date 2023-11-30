class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        indegree = [0] * n 
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        return queue[0] if len(queue) == 1 else -1