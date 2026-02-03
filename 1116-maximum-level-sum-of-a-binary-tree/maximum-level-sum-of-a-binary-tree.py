# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, level, sum_nodes):
            if not node:
                return 
            
            if len(sum_nodes) == level:
                sum_nodes.append(node.val)
            else:
                sum_nodes[level] += node.val

            dfs(node.left, level+1, sum_nodes)
            dfs(node.right, level+1, sum_nodes)

        sum_nodes = []
        dfs(root, 0, sum_nodes)

        max_sum = float('-inf')
        res = 0 

        for i in range(len(sum_nodes)):
            if max_sum < sum_nodes[i]:
                max_sum = sum_nodes[i]
                res = i+1
        return res


            

            