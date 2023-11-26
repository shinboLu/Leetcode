class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        for idx, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))

        prob = [0.0] * n
        prob[start_node] = 1.0

        queue = collections.deque()
        queue.append(start_node)

        while queue:
            curr_node = queue.popleft()
            for next_node, next_prob in graph[curr_node]:

                if prob[curr_node] * next_prob > prob[next_node]:
                    prob[next_node] = prob[curr_node] * next_prob
                    queue.append(next_node)

        return prob[end_node]