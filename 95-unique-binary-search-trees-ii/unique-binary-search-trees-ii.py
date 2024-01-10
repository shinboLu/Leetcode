# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def backtrack(left, right):
            res = []
            if left > right:
                res.append(None)
                return res

            if (left, right) in memo:
                return memo[(left,right)]

            for i in range(left, right+1):
                left_sub_tree = backtrack(left,i - 1)
                right_sub_tree = backtrack(i+1, right)

                for left_node in left_sub_tree:
                    for right_node in right_sub_tree:
                        tree = TreeNode(i, left_node, right_node)
                        res.append(tree)

            memo[(left,right)] = res
            return res
        return backtrack(1, n)
            