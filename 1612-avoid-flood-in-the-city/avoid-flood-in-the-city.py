class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [0] * len(rains)
        dry_days = []  # indices of days when we can dry a lake
        last_rained_day = collections.defaultdict(int)  # lake -> last day it rained

        for day_index, lake in enumerate(rains):
            if lake == 0:  # sunny day, we can choose a lake to dry
                dry_days.append(day_index)
                result[day_index] = 1  # placeholder, to be updated when we choose a lake
            else:  # it rains on lake `lake`
                if lake in last_rained_day:
                    previous_rain_day = last_rained_day[lake]

                    # find the earliest dry day after previous_rain_day
                    dry_pos = bisect.bisect_right(dry_days, previous_rain_day)
                    if dry_pos == len(dry_days):
                        return []  # no valid dry day to avoid flood

                    chosen_dry_day = dry_days[dry_pos]
                    result[chosen_dry_day] = lake
                    dry_days.pop(dry_pos)

                last_rained_day[lake] = day_index
                result[day_index] = -1  # raining day

        return result