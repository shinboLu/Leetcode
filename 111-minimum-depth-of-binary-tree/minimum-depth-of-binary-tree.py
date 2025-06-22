# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def post_order(root):

            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            left_h = post_order(root.left)
            right_h = post_order(root.right)
            if left_h == 0:
                return right_h+1
            elif right_h ==0:
                return left_h+1
            else:
                return min(left_h, right_h)+1

        return post_order(root)

