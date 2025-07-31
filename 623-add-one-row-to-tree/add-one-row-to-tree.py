# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def traverse(node, cur_depth, val, depth):
            if not node:
                return
            if cur_depth == depth-1:
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                new_left.left = node.left
                new_right.right = node.right
                node.left = new_left
                node.right = new_right
            traverse(node.left, cur_depth+1, val, depth)
            traverse(node.right, cur_depth+1, val, depth)
        
        if depth ==1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        traverse(root, 1, val, depth)
        return root
