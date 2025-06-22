# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def postorder(root):
            if not root:
                return True,0
            
            if not root.left and not root.right:
                return True, 1

            # if height_diff <= 1:
            #     return True,height_diff

            isLB, left_h = postorder(root.left)
            isRB, right_h = postorder(root.right)
            if isLB and isRB and abs(left_h - right_h) <= 1:
                return True, max(left_h, right_h)+1
            else:
                return False, max(left_h, right_h)+1
        isBalanced, height = postorder(root)
        return isBalanced