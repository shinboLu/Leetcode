'''
Time: O(log k), space:O(n),对于值和时间戳分别使用两个dict，其value是一个可拓展的list
'''
class TimeMap:

    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        # 因为时间戳是已经sorted，所以可以用bisect
        #bisect([3, 5, 8], 4) 在已sorted的array插入4时，4的idx = 1
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        # index is the first element that is greater than the requested value. 需-1
        return self.data[key][idx - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)