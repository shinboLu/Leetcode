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
            return 
        
        queue = collections.deque([root])

        res = []

        while queue:
            n = len(queue)

            for i in range(n):
                cur_node = queue.popleft()

                if i < n-1:
                    cur_node.next = queue[0]
                elif i == n-1:
                    cur_node.next = None
                
                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)
        return root

                
