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

        def get_root(node):
            if not node.parent:
                return node

            return get_root(node.parent)

        root = get_root(p) 

        def dfs_lca(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node

            left = dfs_lca(node.left)
            right = dfs_lca(node.right)

            if left and right:
                return node
            else:
                return left or right

        return dfs_lca(root)





