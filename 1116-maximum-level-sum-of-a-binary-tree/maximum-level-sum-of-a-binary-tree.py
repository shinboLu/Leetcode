# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append([root, 1])
        maxi = float('-inf')
        res = 1

        while queue:
            n = len(queue)
            level_sum = 0
            for _ in range(n):
                cur_node, level = queue.popleft()
                level_sum += cur_node.val
                if cur_node.left:
                    queue.append([cur_node.left, level+1]) 
                if cur_node.right:
                    queue.append([cur_node.right, level+1])
            if level_sum > maxi:
                res = max(res, level)
                maxi = level_sum
        return res
