# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res 
        tens = 0

        while l1 or l2 or tens != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            cur_sum = l1_val + l2_val + tens
            tens = cur_sum // 10

            newNode = ListNode(cur_sum%10)
            cur.next = newNode
            cur = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

            
