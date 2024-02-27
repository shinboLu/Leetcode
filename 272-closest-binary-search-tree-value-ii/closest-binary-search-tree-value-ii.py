# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)

        res.sort(key = lambda x: abs(x-target))
        print(res)

        return res[:k]