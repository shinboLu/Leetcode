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
            cur_level_sum = 0 

            for _ in range(len(queue)):
                cur = queue.popleft()
                cur_level_sum += cur.val

                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)

            if max_sum < cur_level_sum:
                max_sum, res = cur_level_sum, level

        return res 

