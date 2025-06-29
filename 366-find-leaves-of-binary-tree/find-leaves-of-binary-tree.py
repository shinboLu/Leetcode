# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        global res
        res = [] 

        def dfs_getLeaves_remove(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                res.append(node.val)
                return None
            
            left = dfs_getLeaves_remove(node.left)
            if left is None:
                node.left = None
            right = dfs_getLeaves_remove(node.right)
            if right is None:
                node.right = None
            
            return node

        output = []
        while root is not None:
            if not root.left and not root.right:
                res.append(root.val)
                output.append(res)
                break
            else:
                dfs_getLeaves_remove(root)
                output.append(res)
            res = [] 

        return output