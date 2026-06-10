# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {}
        cur_idx = 0 

        for idx, val in enumerate(inorder):
            inorder_map[val] = idx

        def dfs(left_idx, right_idx):
            nonlocal cur_idx
            if left_idx > right_idx:
                return None
            
            node_val = preorder[cur_idx]
            node = TreeNode(node_val)

            cur_idx +=1

            node.left = dfs(left_idx, inorder_map[node_val]-1) 
            node.right = dfs(inorder_map[node_val]+1, right_idx)
            return node
        return dfs(0, len(inorder)-1)
