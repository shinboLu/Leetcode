class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [x for x in range(numCourses)]
        adj_list = collections.defaultdict(list)
        indegree = [0] * numCourses 

        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1
        queue = collections.deque()
        for idx, degrees in enumerate(indegree):
            if degrees == 0:
                queue.append(idx)
                
        res = []
        while queue:
            cur_course = queue.popleft()
            res.append(cur_course)
            for nei in adj_list[cur_course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []


