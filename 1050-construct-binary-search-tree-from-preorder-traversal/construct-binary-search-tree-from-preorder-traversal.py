# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        preorder_idx = 0
        inorder_map = {val:idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            nonlocal preorder_idx
            if left == right:
                return 
            
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)

            cur_idx = inorder_map[root_val]
            
            preorder_idx += 1

            root.left = dfs(left, cur_idx)
            root.right = dfs(cur_idx+1, right)

            return root 

        return dfs(0, len(preorder))



            
