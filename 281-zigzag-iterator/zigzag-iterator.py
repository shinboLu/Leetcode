class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.count = 1

    def next(self) -> int:
        if self.v1 and self.v2:
            if self.count % 2 == 1:
                self.count += 1
                return self.v1.pop(0)
            else:
                self.count += 1
                return self.v2.pop(0)
            
        elif self.v1 and not self.v2:
            return self.v1.pop(0)
        elif not self.v1 and self.v2:
            return self.v2.pop(0)
        else:
            return 

    def hasNext(self) -> bool:
        return self.v1 or self.v2
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())