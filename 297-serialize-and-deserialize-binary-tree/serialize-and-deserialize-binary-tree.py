# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        def dfs(root):
            nonlocal path
            if not root:
                path.append('None') 
                return 
            path.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(path)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        idx = 0 
        path = data.split(',')

        def dfs(path):
            nonlocal idx
            if path[idx] == 'None':
                idx+=1
                return 
            
            root_val = path[idx]
            root = TreeNode(root_val)
            idx += 1

            root.left = dfs(path)
            root.right = dfs(path)
            return root 
        
        return dfs(path)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))