# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global res 

        res = 0
        def dfs(node, low, high):
            if not node:
                return 
            global res 
            if low <= node.val <= high:
                res += node.val 

            dfs(node.left, low, high)
            dfs(node.right, low, high)

        dfs(root, low, high)
        return res