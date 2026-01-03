class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)

        for a, b in prerequisites:
            adj_list[b].append(a)
        
        visited = [False] * numCourses
        instack = [False] * numCourses

        def dfs(course):
            if instack[course]:
                return True
            if visited[course]:
                return False
            visited[course] = True
            instack[course] = True
            for nei in adj_list[course]:
                if dfs(nei):
                    return True
            instack[course] = False
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True