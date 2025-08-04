# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse_validate(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val:
                return False
            if node.val >= max_val:
                return False
            is_left_valid = traverse_validate(node.left, min_val, node.val)
            is_right_valid = traverse_validate(node.right, node.val, max_val)
            print(is_left_valid, is_right_valid)
            return is_left_valid and is_right_valid

        return traverse_validate(root, float('-inf'), float('inf'))