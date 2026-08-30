# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node after group_prev.
            kth = self.get_kth(group_prev, k)

            # Fewer than k nodes remain.
            if not kth:
                break

            group_next = kth.next

            # Reverse this group.
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Reconnect and advance to the tail of this reversed group.
            old_group_head = group_prev.next
            group_prev.next = kth
            group_prev = old_group_head

        return dummy.next

    def get_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1

        return node
