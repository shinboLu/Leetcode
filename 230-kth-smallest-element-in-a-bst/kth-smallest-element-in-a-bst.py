# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        cur_idx = 0
        def dfs(node):
            nonlocal res, cur_idx
            if not node:
                return 
            
            dfs(node.left)

            cur_idx +=1
            if cur_idx == k:
                res = node.val
                return 
            dfs(node.right)

        dfs(root)

        return res

