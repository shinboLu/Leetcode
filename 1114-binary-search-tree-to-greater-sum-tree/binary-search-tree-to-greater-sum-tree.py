# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_sum = 0 
        def add_val(root):
            if not root:
                return

            add_val(root.right)
            nonlocal cur_sum
            cur_sum += root.val
            root.val = cur_sum 

            add_val(root.left) 

        add_val(root)
        return root

            