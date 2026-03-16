class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        left = 1
        right = 10 ** 18 
        multi = lcm(r[0], r[1])

        while left <= right:
            ## mid is the total time in hours to complete all delivery
            mid = (left+right) //2 

            if d[0] <= mid - mid//r[0] and d[1] <= mid - mid//r[1] and d[0] + d[1] <= mid - mid//multi:
                right = mid -1
            else:
                left = mid +1 

        return left
            

        