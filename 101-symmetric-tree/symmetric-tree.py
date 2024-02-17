# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left_branch, right_branch):
            if not left_branch and not right_branch:
                return True

            if (left_branch and not right_branch) or (not left_branch and right_branch):
                return False
            
            if left_branch.val != right_branch.val:
                return False

            left = dfs(left_branch.left, right_branch.right)
            right = dfs(left_branch.right, right_branch.left)

            return left and right

        return dfs(root.left, root.right)