# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        p_found = False
        q_found = False

        def dfs(node):
            nonlocal p_found, q_found

            if not node:
                return None

            if node == p:
                p_found = True
            if node == q:
                q_found = True

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                return node

            if left and right:
                return node

            return left or right

        res = dfs(root)
        return res if p_found and q_found else None