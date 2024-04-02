class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        if v1 and not v2:
            self.li = v1 
        elif not v1 and v2:
            self.li = v2 
        elif not v1 and not v2:
            self.li = [] 
        else:
            self.li = []
            break_idx = 0 

            for i in range(min(len(v1), len(v2))):
                self.li.append(v1[i])
                self.li.append(v2[i])
                break_idx += 1
            
            self.li.extend(v1[break_idx:]) if break_idx < len(v1) else self.li.extend(v2[break_idx:])

    def next(self) -> int:
        if self.hasNext():
            return self.li.pop(0)


    def hasNext(self) -> bool:
        if self.li:
            return True
        return False
        

        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())