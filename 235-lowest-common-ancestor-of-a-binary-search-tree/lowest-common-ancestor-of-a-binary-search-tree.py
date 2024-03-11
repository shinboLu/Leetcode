# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, val1, val2):
            if not root:
                return None
            # 前序位置
            if root.val == val1 or root.val == val2:
                # 如果遇到目标值，直接返回
                return root
            left = find(root.left, val1, val2)
            right = find(root.right, val1, val2)
            # 后序位置，已经知道左右子树是否存在目标值
            if left and right:
                # 当前节点是 LCA 节点
                return root
            return left if left else right
        return find(root, p.val, q.val)