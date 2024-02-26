# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        def dfs(node):
            if not node:
                return
        left = self.upsideDownBinaryTree(root.left)
        right = self.upsideDownBinaryTree(root.right)
        if root.left:
            root.left.right = root
            root.left.left = root.right
            root.left = root.right = None
        return left if left else root
