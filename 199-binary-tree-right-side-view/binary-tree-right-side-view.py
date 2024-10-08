# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [] 

        queue = collections.deque()
        queue.append(root)

        while queue:
            n = len(queue)
            cur_level = []
            for _ in range(n):
                cur = queue.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            level.append(cur_level)

        res = []

        for l in level:
            res.append(l[-1])

        return res 

