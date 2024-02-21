class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for nodein, nodeout in prerequisites:
            adj[nodeout].append(nodein)
            indegree[nodein] += 1

        queue = collections.deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            cur_class = queue.popleft()
            visited += 1

            for nei in adj[cur_class]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei) 

        return visited == numCourses