class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0,1], [1,0], [-1,0], [0, -1]]
        nrow = len(board)
        ncol = len(board[0])
        visited = set()

        def dfs(x,y,cur_len):
            if cur_len == len(word):
                return True
            if x < 0 or x >= nrow or y < 0 or y >= ncol or board[x][y] != word[cur_len] or (x,y) in visited:
                return False

            visited.add((x,y))
            for nx, ny in dirs:
                if dfs(x+nx, y +ny, cur_len+1):
                    return True
            visited.remove((x,y))
            return False

        for i in range(nrow):
            for j in range(ncol):
                if dfs(i, j, 0):
                    return True
        return False
            