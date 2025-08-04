# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        
        def build(low, high, visited):
            res = []
            if low > high:
                res.append(None)
                return res
            
            if (low,high) in visited:
                return visited[(low, high)]
            
            for i in range(low, high+1):
                left_subtree = build(low, i-1, visited)
                right_subtree = build(i+1, high, visited)
                for left in left_subtree:
                    for right in right_subtree:
                        root = TreeNode(i, left, right)
                        res.append(root)
            return res
        visited = {}
        return build(1, n, visited)
