class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        n = len(batteryPercentages)

        for i in range(n):
            if batteryPercentages[i] >0: 
                res += 1
                for j in range(i+1, n):
                    batteryPercentages[j] = max(0, batteryPercentages[j]-1)

        return res 
