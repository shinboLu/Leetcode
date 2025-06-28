# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs_return_boolean(node, cur_sum):
            if not node:
                return False

            cur_sum+=node.val

            if not node.left and not node.right:
                return cur_sum ==targetSum 

            left = dfs_return_boolean(node.left, cur_sum)
            right = dfs_return_boolean(node.right, cur_sum)

            return left or right
        return dfs_return_boolean(root, 0)
