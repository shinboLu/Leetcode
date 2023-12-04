# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs_return_boolean(root, minVal, maxVal):
            if not root:
                return True
            
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            left = dfs_return_boolean(root.left, minVal, root.val)
            right = dfs_return_boolean(root.right, root.val, maxVal)

            return left and right

        return dfs_return_boolean(root, float('-inf'), float('inf'))