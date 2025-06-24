# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs_return_sum(node, cur_sum):
            if not node:
                return 0

            cur_sum = cur_sum * 10 + node.val

            if not node.left and not node.right:
                return cur_sum

            left_sum = dfs_return_sum(node.left, cur_sum)
            right_sum = dfs_return_sum(node.right, cur_sum)

            return left_sum + right_sum
        return dfs_return_sum(root, 0)
            
