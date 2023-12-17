class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        visited = [False] * len(tiles)
        def backtracking(combs):
            res.add(''.join(combs))

            for i in range(len(tiles)):
                if visited[i]:
                    continue
                visited[i] = True
                combs.append(tiles[i])
                backtracking(combs)
                combs.pop()
                visited[i] = False
        backtracking([])
        print(res )
        return len(res)-1        

                

        