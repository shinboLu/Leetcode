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
    
        def dfs(node, val, visited):
            if node in visited:
                return None 
            if not node:
                return None 
            if node.val == val: 
                return node 
            visited.append(node)
            left = dfs(node.left, val, visited)
            right = dfs(node.right, val, visited)
            if left or right:
                return node 
            parent = dfs(node.parent, val, visited)

            if parent:
                return parent 
            return None 
        
        node = dfs(p, q.val, [])
 
        if node:
            return node 
        node = dfs(q, p.val, [])
        return node 
            