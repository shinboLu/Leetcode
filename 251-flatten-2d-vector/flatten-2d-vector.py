class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.flat = [] 

        for val in vec:
            for num in val:
                self.flat.append(num)
        print(self.flat)
        self.cur_pos = 0

    def next(self) -> int:
        self.cur_pos += 1
        if self.cur_pos-1 < len(self.flat):
            return self.flat[self.cur_pos-1]

    def hasNext(self) -> bool:
        if self.cur_pos < len(self.flat):
            return True
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()