class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [0] * len(rains)
        last_rain = {} 
        sunny_days = []
        for day, lake in enumerate(rains):
            if lake > 0:
                if lake in last_rain:
                    prev = last_rain[lake]
                    pos = bisect.bisect_right(sunny_days, prev)
                    if pos == len(sunny_days):
                        return []
                    drain_day = sunny_days[pos]
                    res[drain_day] = lake
                    sunny_days.pop(pos)
                last_rain[lake] = day
                res[day] = -1
            else:
                sunny_days.append(day)
                res[day] = 1
        return res