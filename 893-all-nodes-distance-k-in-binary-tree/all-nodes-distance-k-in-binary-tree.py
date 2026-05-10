# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_graph = collections.defaultdict(list)
        def build_graph(node, parent):
            if not node:
                return
            
            if node and parent:
                adj_graph[parent.val].append(node.val) 
                adj_graph[node.val].append(parent.val)
            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)                

        build_graph(root, None)
        visited = set([target.val])
        res = []

        def dfs(cur_node_val, distance):
            if distance == k:
                res.append(cur_node_val) 
                return 
            for nei in adj_graph[cur_node_val]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, distance+1)
        dfs(target.val, 0)
        return res
