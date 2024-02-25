# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, path, cur_sum):
            if not root:
                return 
            path.append(root.val)
            cur_sum += root.val
            if not root.left and not root.right and cur_sum == targetSum:
                res.append(path.copy())
            if root.left:
                dfs(root.left, path, cur_sum)
            if root.right:
                dfs(root.right, path, cur_sum)
            path.pop()
            cur_sum -= root.val

        dfs(root, [], 0)
        print(res )
        return res 