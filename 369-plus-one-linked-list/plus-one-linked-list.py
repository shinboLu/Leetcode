# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while head: 
            if head.val != 9:
                cur = head
            head = head.next

        cur.val += 1
        cur = cur.next 

        while cur:
            cur.val = 0 
            cur = cur.next 

        return dummy if dummy.val else dummy.next