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

        mapper = collections.defaultdict(list)
        left_bound = right_bound = 1

        def dfs(root, row, col):
            if root:
                nonlocal left_bound, right_bound
                mapper[col].append((row, root.val))
                left_bound = min(left_bound, col)  
                right_bound = max(right_bound, col)
                dfs(root.left, row+1, col-1)
                dfs(root.right, row+1, col+1)

        dfs(root, 0, 0) 

        res = []
        for col in range(left_bound, right_bound+1):
            mapper[col].sort(key = lambda x: x[0])
            cur_col = [val for row, val in mapper[col]]
            if cur_col:
                res.append(cur_col)

        return res 
            