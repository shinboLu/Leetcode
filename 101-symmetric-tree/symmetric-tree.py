# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs_return_bool(leftT, rightT):
            if not leftT and not rightT:
                return True

            if not leftT or not rightT:
                return False

            if leftT.val != rightT.val:
                return False
            
            left = dfs_return_bool(leftT.left, rightT.right)
            right = dfs_return_bool(leftT.right, rightT.left)

            return left and right

        return dfs_return_bool(root.left, root.right)