from collections import defaultdict
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        d = defaultdict(lambda: defaultdict(lambda: 0))

        for num in nums:
            depth = int(str(num)[0])
            pos = int(str(num)[1])
            val = int(str(num)[2])

            d[depth][pos] = val 

        res = 0

        def dfs(depth, pos, cur_res):
            nonlocal res 
            next_left_pos = pos * 2 -1
            next_right_pos = pos * 2 

            if depth + 1 not in d or next_left_pos not in d[depth+1] and next_right_pos not in d[depth+1]:
                res += cur_res + d[depth][pos]
                return 

            if next_left_pos in d[depth+1]:
                dfs(depth+1, next_left_pos, cur_res+d[depth][pos])
            
            if next_right_pos in d[depth+1]:
                dfs(depth+1, next_right_pos, cur_res + d[depth][pos])

        dfs(1,1,0)

        return res


