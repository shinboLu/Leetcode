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
        global res
        res =float('inf')
        def traverse(root, depth):
            if not root:
                return 
            global res
            if root:
                if not root.left and not root.right:
                    res = min(res, depth)
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)

        traverse(root, 1)
        return res



