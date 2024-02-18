# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)

        before_p = before_head
        after_p = after_head

        while head:
            if head.val < x:
                before_p.next = head
                before_p = before_p.next 

            else:
                after_p.next = head  
                after_p = after_p.next 

            head = head.next 

        after_p.next = None 

        before_p.next = after_head.next

        return before_head.next