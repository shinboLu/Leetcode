# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []
        def dfs(root, level_idx):
            if not root:
                return
            if len(level) == level_idx:
                level.append([])
            
            level[level_idx].append(root.val)
            dfs(root.left , level_idx+1)
            dfs(root.right , level_idx+1)
        dfs(root, 0)
        return level
             
