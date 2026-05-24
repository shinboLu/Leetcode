class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot_tanks = sum(gas) - sum(cost)
        cur_tank = 0
        start = 0 

        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i] 
            if cur_tank < 0:
                start = i+1
                cur_tank= 0 
        if tot_tanks < 0:
            return -1
        return start
