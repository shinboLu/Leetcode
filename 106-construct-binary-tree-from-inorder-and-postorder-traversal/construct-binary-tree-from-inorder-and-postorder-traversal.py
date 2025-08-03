# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.root_idx = len(postorder)-1
        inorder_mapping = {}
        for idx, val in enumerate(inorder):
            inorder_mapping[val] = idx

        def traverse_build(left_idx, right_idx):
            if left_idx > right_idx or self.root_idx < 0:
                return None

            root_val = postorder[self.root_idx]
            root = TreeNode(root_val)
            self.root_idx -=1
            root.right = traverse_build(inorder_mapping[root_val]+1, right_idx)
            root.left = traverse_build(left_idx, inorder_mapping[root_val]-1)
            return root
        return traverse_build(0, len(inorder)-1)