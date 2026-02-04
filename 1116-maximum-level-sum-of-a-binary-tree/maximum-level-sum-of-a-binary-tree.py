# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level, cur_level_sum):
            if not node:
                return
            
            if level == len(cur_level_sum):
                cur_level_sum.append(node.val)
            else:
                cur_level_sum[level] += node.val
            
            dfs(node.left, level+1, cur_level_sum)
            dfs(node.right, level+1, cur_level_sum)

        level_sum = []
        dfs(root, 0, level_sum)

        max_val = float('-inf')
        res = 0 

        for idx, val in enumerate(level_sum):
            if max_val < val:
                max_val = val
                res = idx+1

        return res
        