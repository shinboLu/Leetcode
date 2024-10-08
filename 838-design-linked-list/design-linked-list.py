class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val 

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val )
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0 
        self.size += 1

        prev = self.head

        for _ in range(index):
            prev = prev.next
        newVal = ListNode(val) 
        newVal.next=prev.next
        prev.next = newVal

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        self.size-=1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        prev.next = prev.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)