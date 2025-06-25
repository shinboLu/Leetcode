# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        global res
        res = []

        def dfs_update(node, cur_sum, cur_list):
            global res
            
            if not node:
                return 
            
            cur_list.append(node.val)
            cur_sum += node.val

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    res.append(cur_list.copy())

            dfs_update(node.left, cur_sum, cur_list)
            dfs_update(node.right, cur_sum, cur_list)

            if cur_list:
                cur_list.pop()
            cur_sum -= root.val
        dfs_update(root, 0, [])
        return res

        





