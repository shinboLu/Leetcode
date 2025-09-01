# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(node):
            if not node:
                return 
            
            if node == p or node == q:
                return node
            
            left_node = traverse(node.left)
            right_node = traverse(node.right)

            if left_node and right_node:
                return node
            
            return left_node or right_node
        return traverse(root)