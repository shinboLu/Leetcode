# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0 
        prefix_sum = {0:1}

        def dfs(node, cur_sum):
            nonlocal res
            if not node:
                return
            
            cur_sum += node.val
            
            res += prefix_sum.get(cur_sum-targetSum, 0)
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) +1

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            prefix_sum[cur_sum]-=1
        dfs(root, 0)
        return res
            

