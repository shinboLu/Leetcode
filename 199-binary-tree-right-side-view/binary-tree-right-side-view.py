# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(node, level_idx):
            if not node:
                return 
            
            if len(res) == level_idx:
                res.append(node.val)
            
            dfs(node.right, level_idx+1)
            dfs(node.left, level_idx+1)
        
        dfs(root, 0)
            

        return res
            