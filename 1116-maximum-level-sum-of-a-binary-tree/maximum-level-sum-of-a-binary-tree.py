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
        queue = collections.deque() 
        queue.append(root)
        level_sum = []
        level = 0

        while queue:
            n = len(queue)
            cur_sum = 0

            for _ in range(n):
                cur_node = queue.popleft()
                cur_sum += cur_node.val 

                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)
            
            level+=1

            level_sum.append([cur_sum, level])

        level_sum.sort(key=lambda x: -x[0])
        return level_sum[0][1]


