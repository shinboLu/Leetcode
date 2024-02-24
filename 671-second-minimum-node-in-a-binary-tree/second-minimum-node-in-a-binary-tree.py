# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_v = root.val 
        vals = set()
        def dfs(root):
            if not root:
                return 
            nonlocal vals
            vals.add(root.val) 
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        vals.remove(min_v) 

        return min(vals) if vals else -1 
        


        


            



        
