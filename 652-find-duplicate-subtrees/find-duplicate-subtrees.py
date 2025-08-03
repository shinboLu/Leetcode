# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.visited = {}
        self.res = [] 
        
        def traverse(node):
            if not node:
                return "#"
            
            left = traverse(node.left)
            right = traverse(node.right)

            cur = f"{left},{right},{node.val}"

            freq = self.visited.get(cur, 0)
            if freq == 1:
                self.res.append(node)
            self.visited[cur]=freq+1
            return cur

        traverse(root)
        return self.res
            

            