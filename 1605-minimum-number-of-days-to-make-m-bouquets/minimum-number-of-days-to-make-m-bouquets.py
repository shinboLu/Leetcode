class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def get_num_of_bouqeuts(mid, k):
            num_of_bouquets = 0
            count = 0 

            for day in bloomDay:
                if day <= mid:
                    count+=1
                else:
                    count = 0
                if count ==k:
                    num_of_bouquets +=1
                    count = 0 
            return num_of_bouquets

        left = 0
        right = max(bloomDay)
        min_days = -1
        while left <= right:
            mid = (left+right)//2
            if get_num_of_bouqeuts(mid, k) >= m:
                min_days = mid
                right = mid-1 
            else:
                left = mid+1 
        return min_days
            

