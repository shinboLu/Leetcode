class MRUQueue:

    def __init__(self, n: int):
        self.queue = [x for x in range(1, n+1)]
        
    def fetch(self, k: int) -> int:
        element = self.queue.pop(k-1)
        print(k, element)
        self.queue.append(element)
        return element


        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)