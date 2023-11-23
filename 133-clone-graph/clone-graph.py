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
        visited = {}

        def backtracking(node):
            nonlocal visited
            if not node:
                return node
            
            if node in visited:
                return visited[node]
                
            cloned_node = Node(node.val, [])

            visited[node] = cloned_node

            if node.neighbors:
                cloned_node.neighbors = [backtracking(n) for n in node.neighbors]
            return cloned_node
        
        return backtracking(node)
            