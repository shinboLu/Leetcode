class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letter_set = ['a', 'b', 'c']
        res = []

        def backtracking(idx, curr_comb):
            if len(curr_comb) == n:
                res.append(curr_comb)
                return

            for i in range(len(letter_set)):
                if len(curr_comb) == 0:
                    backtracking(i, curr_comb+letter_set[i])

                else:
                    if curr_comb[-1] == letter_set[i]:
                        continue

                    backtracking(i, curr_comb+letter_set[i])
        backtracking(0, '')

        if k <= len(res):
            return res[k-1]
        
        else:
            return ''
