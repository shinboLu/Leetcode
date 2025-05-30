class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key])

        while left < right:
            mid = (left+right)//2
            if self.store[key][mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return self.store[key][right-1][0] if right !=0 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)