class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_penalty = customers.count('Y')
        cur_penalty = max_penalty
        res = 0
        
        for idx, val in enumerate(customers):
            if val == 'Y':
                cur_penalty-=1
            else:
                cur_penalty +=1
            
            if cur_penalty < max_penalty:
                max_penalty = cur_penalty
                res = idx+1
        return res

