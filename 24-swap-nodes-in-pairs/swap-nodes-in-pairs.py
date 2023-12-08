# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        first_node = head
        second_ndoe = head.next

        first_node.next = self.swapPairs(second_ndoe.next)
        second_ndoe.next = first_node

        return second_ndoe

        
        




