from collections import deque


class HitCounter:

    def __init__(self):
        self.hit_dict = collections.defaultdict(int)
        self.time_lim = 300 
        
    def hit(self, timestamp: int) -> None:
            self.hit_dict[timestamp] +=1 

    def getHits(self, timestamp: int) -> int:
        hit_count = 0 
        for k,v in self.hit_dict.items():
            time_diff = timestamp - k
            if time_diff < 300 and time_diff >= 0:
                hit_count += v
        return hit_count
