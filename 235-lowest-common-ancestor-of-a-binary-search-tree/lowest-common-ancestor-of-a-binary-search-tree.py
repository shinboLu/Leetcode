# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, val1, val2):
            if not root:
                return 

            if root.val > val2:
                return dfs(root.left, val1, val2)
            elif root.val < val1:
                return dfs(root.right,val1, val2)
            else:
                return root
        
        val1 = min(p.val, q.val) 
        val2 = max(p.val, q.val)
        return dfs(root, val1, val2)
