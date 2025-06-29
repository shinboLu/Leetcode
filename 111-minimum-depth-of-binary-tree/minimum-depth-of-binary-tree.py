# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        queue = deque()

        queue.append(root)
        depth = 1

        while queue:
            for cur_lv in range(len(queue)):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
                if not cur.left and not cur.right:
                    return depth
            depth+=1
        