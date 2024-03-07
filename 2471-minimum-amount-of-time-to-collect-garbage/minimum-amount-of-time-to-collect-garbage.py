class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g = 0
        p = 0
        m = 0 

        n = len(garbage)
        tot_time = 0 

        for i in range(n-1, -1, -1):
            cur_house = garbage[i] 
            tot_time += len(cur_house)
            
            if g == 0 and cur_house.find('G') != -1:
                g = i
            
            if p == 0 and cur_house.find('P') != -1:
                p = i
            
            if m == 0 and cur_house.find('M') != -1:
                m = i  

        tot_time += sum(travel[:g]) + sum(travel[:p]) + sum(travel[:m])

        return tot_time
        