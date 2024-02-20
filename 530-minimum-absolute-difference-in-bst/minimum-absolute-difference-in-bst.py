# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorderNodes = [] 

        def inorder(node):
            nonlocal inorderNodes

            if not node:
                return 
            
            inorder(node.left)
            inorderNodes.append(node.val) 
            inorder(node.right)
        
        inorder(root)

        minDiff = float('inf')

        for i in range(1, len(inorderNodes)):
            minDiff = min(minDiff, inorderNodes[i] - inorderNodes[i-1])
        return minDiff