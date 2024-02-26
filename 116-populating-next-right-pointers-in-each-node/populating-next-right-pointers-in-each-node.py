"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node1, node2):
            if not node1 and not node2:
                return 

            node1.next = node2
            dfs(node1.left, node1.right)
            dfs(node1.right, node2.left)
            dfs(node2.left, node2.right)
            
        if not root:
            return 
        dfs(root.left, root.right)
        return root