# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [] 
        queue = collections.deque()
        queue.append(root)
        dir = 0 ## left --> right

        def bfs(queue, dir):
            while queue:
                n = len(queue)
                level_nodes = []
                for _ in range(n):
                    node = queue.popleft()
                    level_nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if dir == 0:
                    res.append(level_nodes)
                    dir=1
                else:
                    res.append(level_nodes[::-1])
                    dir =0
        bfs(queue, dir)
        return res
