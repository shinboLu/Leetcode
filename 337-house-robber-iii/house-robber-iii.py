# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0, 0

            left_rob, left_no_rob = dfs(root.left)
            right_rob, right_no_rob = dfs(root.right)
        
            rob = root.val + left_no_rob + right_no_rob 
            no_rob = max(left_rob, left_no_rob) + max(right_no_rob, right_rob)

        
            return (rob, no_rob)

        return max(dfs(root))