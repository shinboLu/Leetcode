# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def dfs(node):
            if not node:
                return

            if node.val == startValue or node.val == destValue:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right

        
        lca = dfs(root)
        start_path, end_path = '', ''
        queue = collections.deque()
        queue.append((lca, ''))

        while queue:
            node, path = queue.popleft()
            if node.val == startValue:
                start_path = path
            if node.val == destValue:
                end_path = path

            if node.left:
                queue.append((node.left, path + 'L'))
            if node.right:
                queue.append((node.right, path +'R'))

        return 'U' * len(start_path) + end_path
        


            

            

            

