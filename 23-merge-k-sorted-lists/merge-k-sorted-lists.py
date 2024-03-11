# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = [] 
        res = ListNode(-1)
        cur = res 
        for li in lists: 
            while li:
                heappush(hq, li.val)
                li = li.next 

        while hq: 
            cur.next = ListNode(heappop(hq)) 
            cur = cur.next 
        
        return res.next
