# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_maping = {}
        for idx, val in enumerate(inorder):
            inorder_maping[val] = idx

        self.root_idx = 0

        def traverse_build(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            root_val = preorder[self.root_idx]
            root = TreeNode(root_val)

            self.root_idx+=1

            root.left = traverse_build(left_idx, inorder_maping[root_val]-1)
            root.right=traverse_build(inorder_maping[root_val]+1, right_idx)
            return root

        return traverse_build(0, len(inorder)-1)


            