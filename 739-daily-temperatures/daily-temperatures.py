class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for cur_idx, cur_temp in enumerate(temperatures):
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_day = stack.pop() 
                res[prev_day] = cur_idx - prev_day
            stack.append(cur_idx)

        return res