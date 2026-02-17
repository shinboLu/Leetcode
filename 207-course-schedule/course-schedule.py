class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list) 
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            adj_list[b].append(a)
            indegrees[a] +=1
        queue = collections.deque()
        for idx, val in enumerate(indegrees):
            if val == 0:
                queue.append(idx)
        visited = set()
        while queue:
            cur_c = queue.popleft()
            visited.add(cur_c)

            for nei in adj_list[cur_c]:
                indegrees[nei] -=1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return len(visited) == numCourses



