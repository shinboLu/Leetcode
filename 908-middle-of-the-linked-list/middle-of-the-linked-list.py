# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head
        length = 0 
        while right:
            right = right.next
            length+=1
        
        print(length)
        
        if length%2 != 0:
            for i in range(length//2):
                left = left.next
        else:
            for i in range(length//2):
                left = left.next
        return left
