# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def createAllTree(left, right): 
            res = []
            if left > right:
                res.append(None)
                return res
            
            if (left, right) in memo:
                return memo[(left,right)]
            
            for i in range(left, right+1):
                leftSubTree = createAllTree(left, i-1)
                rightSubTree = createAllTree(i+1, right)

                for leftNode in leftSubTree:
                    for rightNode in rightSubTree:
                        root = TreeNode(i, leftNode, rightNode)
                        res.append(root)

            memo[(left, right)] = res
            return res

        return createAllTree(1, n)

            
