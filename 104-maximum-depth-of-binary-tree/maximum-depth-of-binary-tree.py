# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def post_order(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1

            left_h = post_order(root.left)
            right_h = post_order(root.right)

            return max(left_h, right_h)+1
        
        return post_order(root)