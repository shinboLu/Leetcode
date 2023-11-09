class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses

        res = []

        adj_list = collections.defaultdict(list)

        for c1, c2 in prerequisites:
            adj_list[c2].append(c1)
            indegree[c1] += 1
        
        queue = collections.deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue: 
            node = queue.popleft()
            res.append(node)

            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
                
        if len(res) == numCourses:
            return res
        return []
