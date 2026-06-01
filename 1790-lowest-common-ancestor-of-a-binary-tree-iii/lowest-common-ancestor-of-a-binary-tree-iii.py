"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        def dfs(node, target):
            if not node:
                return None
            if node in visited:
                return None

            visited.add(node)
            
            if node == target:
                return node

            left = dfs(node.left, target)
            right = dfs(node.right, target)

            if left or right:
                return node
            
            parent = dfs(node.parent, target)
            if parent:
                return parent
            return None
        
        node = dfs(p, q)
        if node:
            return node
        
        node = dfs(q, p)
        if node:
            return node

            
            
        