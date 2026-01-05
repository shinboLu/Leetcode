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
    def connect(self, root: 'Node') -> 'Node':
        def get_child(node):
            cur = node
            while cur:
                if cur.left:
                    return cur.left
                if cur.right:
                    return cur.right
                cur = cur.next
            return None

        def dfs(node):
            if not node:
                return
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = get_child(node.next)
            if node.right:
                node.right.next = get_child(node.next)

            dfs(node.right)
            dfs(node.left) 
        dfs(root)
        return root