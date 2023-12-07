class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        def bt_is_fibo_eligible(idx, curr_combs):
            if idx == len(num) and len(curr_combs) >= 3:
                return True

            for end_index in range(idx+1, len(num) + 1):
                curr_num = int(num[idx:end_index])
                curr_num_digit = end_index - idx

                if curr_num_digit > 1 and num[idx:end_index][0] == '0':
                    return False
                
                if curr_num > 2 ** 31 -1:
                    return False

                elif len(curr_combs)>= 2 and curr_num > curr_combs[-2] + curr_combs[-1]:
                    return False
                
                elif len(curr_combs) <= 1 or (curr_combs[-2] + curr_combs[-1] == curr_num):
                    curr_combs.append(curr_num)
                    if bt_is_fibo_eligible(idx + curr_num_digit ,curr_combs):
                        return True
                    else: 
                        curr_combs.pop()
            return False
        res = []
        bt_is_fibo_eligible(0, res)
        return res
        
                
            
            