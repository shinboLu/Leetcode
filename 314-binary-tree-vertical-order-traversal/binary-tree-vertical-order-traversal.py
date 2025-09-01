# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_tbl_map = collections.defaultdict(list)
        res = [] 
        start_col = 0
        end_col = 0 

        def dfs(node, r, c):
            if not node:
                return 
            nonlocal start_col, end_col
            col_tbl_map[c].append((node.val, r))
            start_col = min(start_col, c)
            end_col = max(end_col, c)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)

            return 

        dfs(root, 0, 0)

        for col in range(start_col, end_col+1):
            col_tbl_map[col].sort(key = lambda x: x[1])
            col_vals = [val for val, _ in col_tbl_map[col]]
            res.append(col_vals)
        return res
