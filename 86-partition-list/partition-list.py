# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(-1) 
        big = ListNode(-1)
        cur_s = small
        cur_b = big
        p1 = head

        while p1:
            if p1.val < x:
                cur_s.next = p1
                cur_s = cur_s.next
            else:
                cur_b.next = p1
                cur_b = cur_b.next
            temp = p1.next
            p1.next = None
            p1 = temp
        
        cur_s.next = big.next
        return small.next
            

            
                