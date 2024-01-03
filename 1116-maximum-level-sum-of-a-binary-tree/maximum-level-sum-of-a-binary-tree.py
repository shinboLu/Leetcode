# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
updating the maxSum while counting level till the last level
'''
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, res, level = float('-inf'), 0, 0

        queue = collections.deque()
        queue.append(root)

        while queue:
            level += 1
            sum_at_cur_level = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                sum_at_cur_level += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if max_sum < sum_at_cur_level:
                max_sum, res = sum_at_cur_level, level

        return res


