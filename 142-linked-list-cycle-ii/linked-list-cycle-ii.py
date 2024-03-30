# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        visited = set()
        while cur:
            if cur not in visited:
                visited.add(cur)
                cur = cur.next 
            else: 
                return cur
            

        return None