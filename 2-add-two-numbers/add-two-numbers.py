# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_cur = l1
        l2_cur = l2
        carry = 0
        res = ListNode(-1)
        res_p = res

        while l1_cur or l2_cur or carry:
            l1_cur_val = l1_cur.val if l1_cur else 0 
            l2_cur_val = l2_cur.val if l2_cur else 0 

            cur_sum = l1_cur_val + l2_cur_val + carry 

            carry = cur_sum // 10 

            res_p.next = ListNode(cur_sum % 10)
            res_p = res_p.next

            l1_cur = l1_cur.next if l1_cur else None
            l2_cur = l2_cur.next if l2_cur else None
        
        return res.next
            

            