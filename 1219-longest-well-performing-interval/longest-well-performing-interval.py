class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0 
        pre_sum = [0] * (len(hours)+1)

        val_to_idx = {} 

        for i in range(1, len(hours)+1):
            pre_sum[i] = pre_sum[i-1] + (1 if hours[i-1] > 8 else -1)
            if pre_sum[i] not in val_to_idx:
                val_to_idx[pre_sum[i]] = i 


            if pre_sum[i] > 0:
                res = max(res, i)
            else:
                if pre_sum[i] -1 in val_to_idx:
                    j = val_to_idx[pre_sum[i]-1]
                    res = max(res, i-j)

        return res
            

