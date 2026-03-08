class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = 0 
        right = max(bloomDay)

        def check(mid):
            bouquets = 0 
            cur_flower = 0 
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    cur_flower += 1
                else:
                    cur_flower = 0 
                if cur_flower == k:
                    bouquets +=1
                    cur_flower = 0
            return bouquets
        res = -1
        while left <= right:
            mid = (left+right)//2 
            if check(mid) >= m:
                res = mid
                right = mid -1
            else:
                left = mid + 1
        return res







