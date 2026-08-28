class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        nrows = len(grid)
        ncols = len(grid[0])

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] ==1:
                    rows.append(row)
                    cols.append(col)
        rows.sort()
        cols.sort()

        mid = len(rows)//2
        meeting_row = rows[mid]
        meeting_col = cols[mid]

        tot_dist = 0 
        for r in rows:
            tot_dist += abs(r-meeting_row)
        for c in cols:
            tot_dist+=abs(c-meeting_col)

        return tot_dist
                