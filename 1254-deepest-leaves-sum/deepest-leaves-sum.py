# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = 0 
        tot_sum = 0
        def dfs(level, root):
            if not root:
                return 

            dfs(level+1, root.left)
            dfs(level+1, root.right)

            nonlocal max_level, tot_sum

            if level > max_level:
                max_level = level 
                tot_sum = 0 
            
            if level == max_level:
                tot_sum += root.val
            
            
        dfs(0, root) 
        return tot_sum
            