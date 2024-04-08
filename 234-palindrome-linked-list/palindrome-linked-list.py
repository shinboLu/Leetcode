# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head

        def traverse(right):
            nonlocal left
            if not right: 
                return True 
            
            res = traverse(right.next) 

            res = res and (right.val == left.val)
            left = left.next 

            return res 

        return traverse(head)

        



