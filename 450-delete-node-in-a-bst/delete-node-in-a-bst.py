# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(node):
            while node.left != None:
                node = node.left
            return node
        def travese_delete(node, key):
            if not node:
                return 
            if node.val == key:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                
                min_node = getMin(node.right)
                node.right = travese_delete(node.right,min_node.val)
                min_node.left = node.left
                min_node.right = node.right
                node = min_node
            elif node.val > key:
                node.left = travese_delete(node.left, key)
            elif node.val < key:
                node.right = travese_delete(node.right, key)
            return node
        
        return travese_delete(root, key)
                

            