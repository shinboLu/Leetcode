# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        ans = []

        def bfs(root):
            queue = collections.deque()
            queue.append(root)

            while queue:
                level_val = []
                n = len(queue)
                for i in range(n):
                    curr = queue.popleft()
                    level_val.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                res.append(level_val)

        bfs(root)

        for level in res:
            ans.append(max(level))
        
        return ans 
            

        
        






