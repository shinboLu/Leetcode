class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        visited = [False] * len(tiles)
        res = set() 

        def backtrack(combs):
            res.add(''.join(combs))

            for i in range(len(tiles)):
                if visited[i]:
                    continue

                visited[i] = True
                combs.append(tiles[i])
                backtrack(combs)
                combs.pop()
                visited[i] = False
        backtrack([])

        return len(res)-1


        