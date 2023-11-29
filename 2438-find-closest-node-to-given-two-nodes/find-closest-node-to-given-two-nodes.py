class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        reachable1 = collections.defaultdict(int)
        reachable2 = collections.defaultdict(int)
        reachable1[node1] = 0
        curr = node1
        steps = 0
        while edges[curr] != -1:
            curr = edges[curr]
            steps += 1
            if curr in reachable1:
                break
            reachable1[curr] = steps
        
        reachable2[node2] = 0
        curr = node2
        steps = 0
        while edges[curr] != -1:
            curr = edges[curr]
            steps += 1
            if curr in reachable2:
                break
            reachable2[curr] = steps
        result = float('inf')
        result_node = -1
        for node in reachable1.keys():
            if node in reachable2:
                if result > max(reachable1[node], reachable2[node]):
                    result = max(reachable1[node], reachable2[node])
                    result_node = node
                elif result == max(reachable1[node], reachable2[node]):
                    result_node = min(node, result_node)
        
        return result_node
        