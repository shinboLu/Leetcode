"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node 

        visited = {} 
        queue = collections.deque()
        queue.append(node)
        visited[node] = Node(node.val, [])

        while queue:
            cur_node = queue.popleft()
            for nei in cur_node.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    queue.append(nei)
                visited[cur_node].neighbors.append(visited[nei])

        return visited[node]

                
