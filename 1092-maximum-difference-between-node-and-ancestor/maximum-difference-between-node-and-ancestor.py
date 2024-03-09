# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root, cur_max, cur_min):
            if not root:
                return cur_max - cur_min
            
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val) 

            left = dfs(root.left, cur_max, cur_min)
            right = dfs(root.right, cur_max, cur_min)
            return max(left, right)

        return dfs(root, root.val, root.val)
            


            

            