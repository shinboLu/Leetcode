class TicTacToe:

    def __init__(self, n: int):
        self.board, self.size = [ [0] * n for _ in range(n) ], n
        
    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] != 0: return 0
        
        self.board[row][col] = player
        
        def r()-> bool:
            return sum(1 for j in range(self.size) if self.board[row][j] == player) == self.size

        def c() -> bool:
            return sum(1 for i in range(self.size) if self.board[i][col] == player) == self.size

        def d() -> bool:
            return sum(1 for i in range(self.size) if self.board[i][i] == player) == self.size

        def ad() -> bool:
            return sum(1 for i in range(self.size - 1, -1, -1) if self.board[i][self.size - i - 1] == player) == self.size
        
        return player if (r() or c() or d() or ad()) else 0