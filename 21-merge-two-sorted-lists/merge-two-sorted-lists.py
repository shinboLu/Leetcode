# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy_head = ListNode(0) 
        cur = dummy_head

        while l1 and l2: 
            if l1.val <= l2.val:
                cur.next = l1 
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
        cur.next = l1 if l1 else l2

        return dummy_head.next

         
                

        
        
        
        