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
        level_container = [] 
        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level_container.append(level)
        res = []
        for level in level_container:
            level_max = max(level)
            res.append(level_max)
        return res 



