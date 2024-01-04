class ListNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode
        

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        
        return self.current.key

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -=1 
        return self.current.key
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)