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
        self.visited = {}

        def dfs(cur_node):
            if not cur_node:
                return None
            if cur_node in self.visited:
                return self.visited[cur_node]
            self.visited[cur_node] = Node(cur_node.val)

            for nei in cur_node.neighbors:
                neis = dfs(nei)
                self.visited[cur_node].neighbors.append(neis) 
            return self.visited[cur_node]
            
        return dfs(node)
                

