class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        
        for num in nums:
            depth = int(str(num)[0])
            pos = int(str(num)[1])
            val = int(str(num)[2])

            node = TreeNode(val)

            tree[(depth, pos)] = node

            if depth == 1:
                root = node

            else:
                parent = tree[(depth-1, (pos+1)//2)]

                if pos % 2 == 1:
                    parent.left = node
                else:
                    parent.right = node

        res=0

        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.left:
                    stack.append((node.left, val + node.left.val))
                if node.right:
                    stack.append((node.right, val + node.right.val))
        return res 


