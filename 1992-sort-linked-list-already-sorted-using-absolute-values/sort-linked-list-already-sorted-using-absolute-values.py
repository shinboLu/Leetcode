# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = head

        while cur.next:
            if cur.val > cur.next.val:
                dummy = cur.next
                cur.next = dummy.next
                dummy.next = head
                
                head = dummy
            else:
                cur = cur.next

        return head

