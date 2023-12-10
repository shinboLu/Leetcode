class Solution:
    def numTilePossibilities(self, tiles: str) -> int: 
        res = set()

        def backtracking(t, curr , index):
            if index == len(curr):
                res.add(curr)
                return 

            for i in range(len(t)):
                backtracking(t[:i] + t[i+1:], curr+t[i], index)

        for i in range(1, len(tiles)+1):
            backtracking(tiles, '', i)
        return len(res)
         


        # record = [0] * 26

        # for tile in tiles:
        #     record[ord(tile) - ord('A')] += 1

        # print(record)
        
        # def dfs(record):
        #     s = 0 
        #     for i in range(26):
        #         if not record[i]:
        #             continue
        #         record[i] -= 1
        #         s += dfs(record) + 1
        #         record[i] += 1
        #     return s

        # return dfs(record)




            
