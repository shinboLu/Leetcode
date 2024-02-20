# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 

        queue = collections.deque()
        queue.append(root) 
        res = []

        while queue:
            n = len(queue)
            cur_level = []

            for i in range(n):
                cur = queue.popleft()
                cur_level.append(cur.val)

                if cur.left:
                    queue.append(cur.left) 

                if cur.right:
                    queue.append(cur.right)
            res.append(cur_level)

        return res 