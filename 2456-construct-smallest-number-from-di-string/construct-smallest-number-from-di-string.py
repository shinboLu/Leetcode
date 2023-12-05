class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = None

        def backtracking_update_res(start, comb):
            nonlocal res
            n = len(pattern)
            if res:
                return

            if start == n:
                res = ''.join(str(item) for item in comb)
                return 

            last_digit = comb[-1]
            for i in range(1, 10):
                appended = False
                if pattern[start] == 'I' and i > last_digit and i not in comb:
                    appended = True
                    comb.append(i)
                    backtracking_update_res(start + 1, comb)
                elif pattern[start] == 'D' and i < last_digit and i not in comb:
                    appended = True
                    comb.append(i)
                    backtracking_update_res(start+1, comb)

                if appended:
                    comb.pop(-1)

        for i in range(1, 10):
            if not res:
                backtracking_update_res(0, [i])
        return res
                
            


            

            


