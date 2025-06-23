# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs_return_root_same(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val == root2.val:
                left_nodes = dfs_return_root_same(root1.left, root2.left) 
                right_nodes = dfs_return_root_same(root1.right, root2.right)

                if left_nodes and right_nodes:
                    return True
                else:
                    return False
            else:
                return False
        

        res = dfs_return_root_same(p, q)

        return res
            
