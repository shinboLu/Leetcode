# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(root, max_len):
            if not root:
                return 
            nonlocal res
            res = max(res, max_len)
            if root.left:
                if root.left.val == root.val + 1:
                    dfs(root.left, max_len + 1)

                else:
                    dfs(root.left,1)

            if root.right:
                if root.right.val == root.val + 1:
                    dfs(root.right, max_len +1)
                else:
                    dfs(root.right, 1)                
        dfs(root, 1)

        return 0 if not root else res
            