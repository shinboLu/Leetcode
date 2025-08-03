# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cur_val = 0 

        def traverse(node):
            if not node:
                return 0
            
            traverse(node.right)
            self.cur_val += node.val 
            node.val = self.cur_val
            traverse(node.left)

        traverse(root)
        return root