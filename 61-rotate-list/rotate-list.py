# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        cur = head
        count = 1
        while cur.next:
            count +=1
            cur = cur.next

        cur.next = head
        k = count - (k % count)

        while k > 0:
            cur = cur.next
            k-=1
        
        res = cur.next
        cur.next = None

        return res

        