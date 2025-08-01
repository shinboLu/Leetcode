# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def travese(nums):
            if not nums:
                return 
            max_idx = nums.index(max(nums))
            left_nodes = nums[:max_idx]
            right_nodes = nums[max_idx+1:]
            root = TreeNode(nums[max_idx])

            root.left = travese(left_nodes)
            root.right = travese(right_nodes)

            return root

        return travese(nums)
