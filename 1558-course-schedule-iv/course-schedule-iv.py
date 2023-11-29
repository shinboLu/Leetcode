from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ## edge case
        if not prerequisites:
            return [False] * len(queries)

        pre_lookup = defaultdict(set)
        adj_list = defaultdict(list)
        
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegree[v] += 1
        print(adj_list)
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            #print(queue)
            curr = queue.popleft()
            for next_class in adj_list[curr]:
                pre_lookup[next_class].add(curr)
                pre_lookup[next_class].update(pre_lookup[curr])

                indegree[next_class] -=1
                if indegree[next_class] == 0:
                    queue.append(next_class)
        result = [True if q[0] in pre_lookup[q[1]] else False for q in queries]

        return result
                    

