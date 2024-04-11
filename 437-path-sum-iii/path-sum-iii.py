# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        freq_map = collections.defaultdict(int)
        def preorder(root, cursum):
            nonlocal count

            if not root:
                return 
            cursum += root.val
            if cursum == targetSum:
                count += 1
            
            count += freq_map[cursum-targetSum]
            freq_map[cursum] += 1

            preorder(root.left, cursum)
            preorder(root.right, cursum)

            freq_map[cursum] -= 1
        preorder(root, 0)
        return count 






        
