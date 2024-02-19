"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val,None, None) 
                return self.visited[node]
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        cur = head  

        new_node = Node(cur.val, None, None)
        self.visited[cur] = new_node 

        while cur:
            new_node.next = self.getClonedNode(cur.next)
            new_node.random = self.getClonedNode(cur.random) 

            cur = cur.next 
            new_node = new_node.next 

        return self.visited[head]


        

        