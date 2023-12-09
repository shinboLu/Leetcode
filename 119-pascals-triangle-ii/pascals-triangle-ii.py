class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex +1)

        if rowIndex == 0:
            return res

        prev_row = self.getRow(rowIndex-1)
        for i in range(1, len(res)-1):
            res[i] = prev_row[i-1] + prev_row[i]

        return res