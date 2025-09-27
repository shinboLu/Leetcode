class HitCounter:

    def __init__(self):
        self.counter = collections.defaultdict(int)
    def hit(self, timestamp: int) -> None:
        self.counter[timestamp] += 1
    
    def getHits(self, timestamp: int) -> int:
        res = 0
        if timestamp > 300:
            stop = timestamp - 300
            for i in range(timestamp, stop , -1):
                res += self.counter[i]
        else:
            for i in range(timestamp, -1, -1):
                res += self.counter[i]
        return res
        

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)