# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    
        res = None 

        while root:
            if p.val >= root.val:
                root = root.right 
            
            else: 
                res = root 
                root = root.left 

        return res 