# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        global min_dept 
        min_dept= float('inf')

        def dfs_return_dep(root, cur_depth):
            global min_dept
            if not root:
                return 

            if not root.left and not root.right:
                min_dept = min(min_dept, cur_depth)
            
            dfs_return_dep(root.left, cur_depth+1)
            dfs_return_dep(root.right, cur_depth+1)

        dfs_return_dep(root, 1)
        return min_dept
    