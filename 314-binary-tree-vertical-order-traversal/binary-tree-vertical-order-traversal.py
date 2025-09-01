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
        start_col = 0 
        end_col = 0 

        def dfs(node, r, c ):
            nonlocal start_col, end_col, col_tbl_map
            if not node:
                return

            col_tbl_map[c].append((r,node.val))
            start_col = min(start_col, c)
            end_col = max(end_col, c)

            dfs(node.left, r + 1, c -1)
            dfs(node.right, r + 1, c +1)
        dfs(root, 0, 0)
        res = [] 
        for col in range(start_col, end_col+1):
            col_tbl_map[col].sort(key=lambda x: x[0])
            col_val = [val for row, val in col_tbl_map[col]]
            res.append(col_val)
        return res 