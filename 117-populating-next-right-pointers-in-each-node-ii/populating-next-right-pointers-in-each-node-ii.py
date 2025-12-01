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
        if not root:
            return None
        queue = collections.deque()

        queue.append(root)

        while queue:
            n = len(queue)
            pre_node = None
            for _ in range(n):
                cur=queue.popleft()
                if pre_node:
                    pre_node.next = cur
                pre_node = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right) 
        return root
