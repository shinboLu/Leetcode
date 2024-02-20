# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque()
        queue.append(root)

        res = [] 

        while queue:
            n = len(queue)
            cur_level_val = [] 
            cur_level_count = 0

            for _ in range(n):
                cur_level_count += 1
                cur_node = queue.popleft()
                cur_level_val.append(cur_node.val) 

                if cur_node.left:
                    queue.append(cur_node.left) 
                if cur_node.right:
                    queue.append(cur_node.right) 
            res.append(float(sum(cur_level_val) / cur_level_count)) 
        return res 