# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        global res 
        res = []

        def dfs_return(node,k):
            if not node:
                return 
            global res
            res.append(node.val)
            dfs_return(node.left, k)
            dfs_return(node.right, k)
        dfs_return(root, k)
        res = sorted(res)
        print(res)

        return res[k-1]            