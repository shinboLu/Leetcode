# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        res = ListNode(0)
        dummy = res

        l1_p = l1
        l2_p = l2

        while l1_p or l2_p or carry:
            l1_val = l1_p.val if l1_p else 0 
            l2_val = l2_p.val if l2_p else 0 
            cur_sum = l1_val + l2_val + carry
            cur_digit = cur_sum % 10
            carry = cur_sum // 10
            dummy.next = ListNode(cur_digit)
            dummy = dummy.next
            l1_p = l1_p.next if l1_p else None
            l2_p = l2_p.next if l2_p else None
        return res.next


            
