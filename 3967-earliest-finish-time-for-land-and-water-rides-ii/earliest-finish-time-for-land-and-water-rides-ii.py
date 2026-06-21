class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterDuration)
        INF = float('inf')

        # Layer 1: compute earliest finish time for each ride done first
        land_ft  = [landStartTime[i]  + landDuration[i]  for i in range(n)]
        water_ft = [waterStartTime[j] + waterDuration[j] for j in range(m)]

        # Layer 2: for each first-ride node, find the best second ride
        # Exactly like "for each course, propagate to dependent courses"
        ans = INF

        # Order: land first → water second
        # min_land = best (minimum) finish time across all land first-rides
        # Then for each water ride, compute finish time given min_land
        min_land = min(land_ft)
        for j in range(m):
            finish = max(min_land, waterStartTime[j]) + waterDuration[j]
            ans = min(ans, finish)

        # Order: water first → land second
        min_water = min(water_ft)
        for i in range(n):
            finish = max(min_water, landStartTime[i]) + landDuration[i]
            ans = min(ans, finish)

        return ans