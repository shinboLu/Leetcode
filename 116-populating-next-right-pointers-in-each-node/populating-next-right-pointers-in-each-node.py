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
        if not root:
            return
        def traverse(l_node, r_node):
            if not l_node and not r_node:
                return
            
            l_node.next = r_node

            traverse(l_node.left, l_node.right) 
            traverse(r_node.left, r_node.right)
            traverse(l_node.right, r_node.left)
        traverse(root.left, root.right)
        return root