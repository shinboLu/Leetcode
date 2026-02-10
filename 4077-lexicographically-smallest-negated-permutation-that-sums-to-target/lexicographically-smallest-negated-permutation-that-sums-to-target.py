class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        def sum_up_to(x):
            return x * (x+1) //2

        cur_sum = sum_up_to(n)
        if target < -cur_sum or target > cur_sum:
            return [] 

        vals = []

        for i in range(n, 0, -1):
            if sum_up_to(i-1) - i >= target:
                target += i
                vals.append(-i) 

            else:
                target -= i 
                vals.append(i)
        
        if target != 0:
            return [] 
        
        vals.sort()
        return vals
        