# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def update_root(node):
            if not node:
                return 

            if not node.left and not node.right:
                return node 

            left = update_root(node.left)
            right = update_root(node.right)

            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            return right if right else left
        
        update_root(root)