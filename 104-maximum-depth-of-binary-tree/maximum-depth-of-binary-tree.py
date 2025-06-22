# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        global res 

        res = 0

        def topdown(root, depth):
            global res
            if not root:
                return 
            if not root.left and not root.right:
                res = max(res, depth)

            topdown(root.left, depth+1)
            topdown(root.right, depth+1)

        topdown(root, 1)
        return res
