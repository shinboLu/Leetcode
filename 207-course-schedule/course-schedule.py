class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)

        for c,p_c in prerequisites:
            adj_list[p_c].append(c)

        visited = [False] * numCourses
        in_stack = [False] * numCourses

        def dfs(cur_c, visited, in_stack):
            if in_stack[cur_c]:
                return False

            if visited[cur_c]:
                return True
            
            in_stack[cur_c] = True
            visited[cur_c] = True
            for n_c in adj_list[cur_c]:
                if not dfs(n_c, visited, in_stack):
                    return False
            in_stack[cur_c] = False
            return True

        for i in range(numCourses):
            if not dfs(i, visited, in_stack):
                return False
        return True