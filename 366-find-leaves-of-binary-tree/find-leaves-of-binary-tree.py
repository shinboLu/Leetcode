# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        global res
        global output
        res = [] 
        output = []

        def dfs_remove_node(node):
    
            if not node:
                return None

            if not node.left and not node.right:
                res.append(node.val)
                return None 
            
            left = dfs_remove_node(node.left)
            right = dfs_remove_node(node.right)
            if not left:
                node.left = None 
            if not right:
                node.right = None 


            return node 

        while root is not None:
            if not root.left and not root.right:
                output.append([root.val])
                break
            else:
                # print(root)
                dfs_remove_node(root)
                output.append(res)
                res = []


            

        return output 


      