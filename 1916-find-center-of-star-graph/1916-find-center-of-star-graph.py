class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertices = len(edges)
        adjList = collections.defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        for k, v in adjList.items():
            if len(v) == vertices:
                return k
        return -1

            