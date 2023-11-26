class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        graph = collections.defaultdict(list)
        res = [0] * len(edges)
        for idx, val in enumerate(edges):
            graph[val].append(idx)

        for k ,v in graph.items():
            for node in v:
                res[k] += node

        return res.index(max(res))
        


        
        