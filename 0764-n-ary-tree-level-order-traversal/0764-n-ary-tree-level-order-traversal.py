"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        res.append([root.val])
        visited = set()
        while len(queue) > 0:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                for child in node.children:
                    if child:
                        level.append(child.val)
                        queue.append(child)
            if len(level) > 0:
                res.append(level)
        return res 
                
        