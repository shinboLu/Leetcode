class MinStack:

    def __init__(self):
        self.res = [] 
        self.cur_min = float('inf')
    def push(self, val: int) -> None:
        if not self.res:
            self.res.append([val, val])
            return

        self.cur_min = min(self.res[-1][1], val)
        self.res.append([val, self.cur_min])

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1][0]

    def getMin(self) -> int:
        return self.res[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()