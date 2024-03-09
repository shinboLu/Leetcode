# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        root_idx = 0 
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        
        def dfs(left, right):
            if left == right:
                return 

            nonlocal root_idx
            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            root_idx += 1

            cur_idx = inorder_map[root_val]

            root.left = dfs(left, cur_idx)
            root.right = dfs(cur_idx+1, right)

            return root 
        
        return dfs(0, len(preorder))






            
