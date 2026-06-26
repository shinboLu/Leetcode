class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        all_min = []

        for devices in units:
            devices.sort()
            if len(devices) == 1:
                all_min.append([devices[0], 0])
            else:
                all_min.append([devices[0], devices[1]])

        global_min = min(m[0] for m in all_min)
        sum_of_1st_mins = sum(m[0] for m in all_min)
        sum_of_2nd_mins = sum(m[1] for m in all_min)

        best = sum_of_1st_mins  # <-- doing nothing is always a valid option

        for first, second in all_min:
            candidate = sum_of_2nd_mins - second + global_min
            best = max(best, candidate)

        return best