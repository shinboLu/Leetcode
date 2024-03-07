class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        nrow = len(grid)
        ncol = len(grid[0])

        diff = [[0] * ncol for _ in range(nrow)]
        onesRow = []
        zerosRow = []
        for row in range(nrow):
            onesRow.append(grid[row].count(1))
            zerosRow.append(grid[row].count(0))
        #print(onesRow, zerosRow)

        cols = []

        for col in range(ncol):
            cur_col = []
            for row in range(nrow):
                cur_col.append(grid[row][col])
            cols.append(cur_col)

        onesCol = []
        zerosCol = []

        for col in cols:
            onesCol.append(col.count(1))
            zerosCol.append(col.count(0))

        
        for row in range(nrow):
            for col in range(ncol):
                diff[row][col] = onesRow[row] + onesCol[col] - zerosRow[row] - zerosCol[col]

        return diff



