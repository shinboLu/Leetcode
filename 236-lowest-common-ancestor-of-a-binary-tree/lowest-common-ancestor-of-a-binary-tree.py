# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs_return_node(node):
            if not node:
                return 

            if node == p or node == q:
                return node

            left_match = dfs_return_node(node.left)
            right_match = dfs_return_node(node.right)

            if left_match and right_match:
                return node
            
            return left_match if not right_match else right_match


        return dfs_return_node(root)

            