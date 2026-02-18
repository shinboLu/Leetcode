"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        res = Node(-1)
        cur = res

        mapping = {}

        while dummy:
            new_node = Node(dummy.val)
            mapping[dummy] = new_node
            cur.next = new_node
            cur = cur.next
            dummy = dummy.next

        dummy = head
        cur = res.next
        while dummy:
            if dummy.random:
                cur.random = mapping[dummy.random]
            else:
                cur.random = None
            dummy = dummy.next
            cur = cur.next 

        return res.next
