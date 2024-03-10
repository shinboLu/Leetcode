# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are equal in value and structure
        def checkEqual(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return checkEqual(root1.left, root2.left) and checkEqual(root1.right, root2.right)
        
        # Traverse through the root tree and check if any subtree matches the subRoot tree
        if not root:
            return False
        elif checkEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)