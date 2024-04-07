# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        res = 0 

        def dfs(root, distance):
            nonlocal res
            if not root:
                return [] 

            if not root.left and not root.right:
                return [1]

            left = dfs(root.left, distance)
            right = dfs(root.right, distance)

            for i in left:
                if i >= distance:
                    continue 
                for j in right:
                    if i + j <= distance:
                        res += 1

            return [1 + i for i in left + right]
        dfs(root, distance)

        return res 
