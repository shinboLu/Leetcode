# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# return node which equals to the val
# exit: not root, return None
# 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def recursion(root):
            if not root:
                return
            
            if root.val < val:
                return recursion(root.right)
            
            elif root.val > val:
                return recursion(root.left)
            else:
                return root

        return recursion(root)

            

            

