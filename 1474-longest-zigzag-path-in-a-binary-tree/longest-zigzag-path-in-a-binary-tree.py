# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root,go_left, cur_len):
            if not root:
                return 
            nonlocal res 

            res = max(res, cur_len)

            if go_left:
                dfs(root.left, False, cur_len+1)
                dfs(root.right, True, 1)

            else: 
                dfs(root.left, False, 1)
                dfs(root.right, True, cur_len+1)

        dfs(root, False, 0)
        dfs(root, True, 0)

        return res


            


            

            