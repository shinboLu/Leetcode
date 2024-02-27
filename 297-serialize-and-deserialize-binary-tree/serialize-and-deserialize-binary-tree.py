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
        def preOrder(root):
            if not root:
                path.append('None')
                return 
            path.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right) 

        preOrder(root)

        return ','.join(path)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def decode(data):
            if data[0] == 'None':
                data.pop(0)
                return None 

            root = TreeNode(data[0])
            data.pop(0)
            root.left = decode(data)
            root.right = decode(data) 
            return root
        data_list = data.split(',')
        return decode(data_list)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))