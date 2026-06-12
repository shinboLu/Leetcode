class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        left = 1
        right = max(bloomDay)

        def calc_bouquets(curday):
            tot_bouquets = 0 
            cur_flower_count = 0 
            for day in bloomDay: 
                if day <= curday: 
                    cur_flower_count += 1
                else:
                    cur_flower_count = 0
                if cur_flower_count == k:
                    tot_bouquets +=1
                    cur_flower_count = 0
                
            return tot_bouquets

        while left < right:
            cur_day = (left+right)//2 
            tot_bouquets = calc_bouquets(cur_day)
            if tot_bouquets < m:
                left = cur_day+1
            else: 
                right = cur_day

        return left 

